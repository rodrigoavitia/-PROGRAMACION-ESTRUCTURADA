from conexionBD_llantas import *
import pandas as pd
import openpyxl

def agregar_llanta(usuario_id, marca, categoria, medida, estado, precio, cantidad):
    try:
        cursor.execute("""
            INSERT INTO llantas (usuario_id, marca, categoria, medida, estado, precio, cantidad)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (usuario_id, marca, categoria, medida, estado, precio, cantidad))
        conexion.commit()
        return True
    except Exception as e:
        print("Error al agregar llanta:", e)
        return False

def mostrar_llantas(usuario_id):
    try:
        cursor.execute("SELECT * FROM llantas WHERE usuario_id = %s", (usuario_id,))
        return cursor.fetchall()
    except Exception as e:
        print("Error al mostrar llantas:", e)
        return []

def buscar_llanta(usuario_id, marca):
    try:
        cursor.execute("SELECT * FROM llantas WHERE usuario_id = %s AND marca LIKE %s", (usuario_id, "%" + marca + "%"))
        return cursor.fetchall()
    except Exception as e:
        print("Error al buscar llantas:", e)
        return []

def eliminar_llanta(usuario_id, llanta_id):
    try:
        cursor.execute("DELETE FROM llantas WHERE usuario_id = %s AND id = %s", (usuario_id, llanta_id))
        conexion.commit()
        return cursor.rowcount > 0
    except Exception as e:
        print("Error al eliminar llanta/ No existe:", e)
        return False
    

    
def vender_llanta(usuario_id, id_llanta, cantidad_vender):
    try:
        cursor = conexion.cursor()
        
        # 1. Verificar stock y obtener precio de la llanta
        cursor.execute("""
            SELECT l.cantidad, l.precio 
            FROM llantas l 
            WHERE l.id=%s AND l.usuario_id=%s
        """, (id_llanta, usuario_id))
        
        resultado = cursor.fetchone()
        if not resultado:
            cursor.close()
            return "no_llanta"
            
        stock_actual, precio_unitario = resultado
        
        # 2. Validar stock suficiente
        if cantidad_vender > stock_actual:
            cursor.close()
            return "no_stock"
        
        # 3. Calcular total de la venta
        total_venta = precio_unitario * cantidad_vender
        
        # 4. Actualizar stock en llantas
        nuevo_stock = stock_actual - cantidad_vender
        cursor.execute("""
            UPDATE llantas 
            SET cantidad=%s 
            WHERE id=%s AND usuario_id=%s
        """, (nuevo_stock, id_llanta, usuario_id))
        
        # 5. Registrar la venta en la tabla de registro_ventas
        cursor.execute("""
            INSERT INTO registro_ventas (
                llanta_id, 
                usuario_id, 
                cantidad, 
                total, 
                fecha
            ) VALUES (%s, %s, %s, %s, CURDATE())
        """, (id_llanta, usuario_id, cantidad_vender, total_venta))
        
        conexion.commit()
        cursor.close()
        return "ok"
        
    except Exception as e:
        print(f"Error al vender llanta: {e}")
        conexion.rollback()
        return "error"
    
def mostrar_ventas(usuario_id):
    try:
        cursor.execute("""
            SELECT rv.id, l.marca, rv.cantidad, rv.total, rv.fecha 
            FROM registro_ventas rv 
            JOIN llantas l ON rv.llanta_id = l.id 
            WHERE l.usuario_id = %s
        """, (usuario_id,))
        return cursor.fetchall()
    except Exception as e:
        print("Error al mostrar ventas:", e)
        return [] 
    

import pandas as pd
from datetime import datetime
#----------------------------------------------------------------------------------------------------------------
def exportar_a_excel():
    try:
        # 1. Obtener datos con nombres de columnas
        cursor = conexion.cursor()
        
        # Tabla llantas
        cursor.execute("SELECT * FROM llantas")
        llantas = cursor.fetchall()
        columnas_llantas = [i[0] for i in cursor.description]  # Nombres de columnas
        
        # Tabla ventas
        cursor.execute("SELECT * FROM registro_ventas")
        ventas = cursor.fetchall()
        columnas_ventas = [i[0] for i in cursor.description]   # Lista por Comprensión Una lista por comprensión es una forma concisa y elegante de
                                                               # crear listas en Python. Permite generar una nueva lista aplicando una expresión a cada elemento de un iterable,
                                                               # (como una lista, tupla, rango, etc.), opcionalmente filtrando elementos con una condición.
        cursor.close()

        # 2. Crear Excel con pandas
        nombre_archivo = "reporte_llantas.xlsx"
        
        with pd.ExcelWriter(nombre_archivo) as writer:
            # Hoja Llantas
            pd.DataFrame(llantas, columns=columnas_llantas).to_excel(
                writer, sheet_name='Llantas', index=False
            )
            
            # Hoja Ventas
            pd.DataFrame(ventas, columns=columnas_ventas).to_excel(
                writer, sheet_name='Ventas', index=False
            )

        print(f"\nArchivo creado: {nombre_archivo}")
        return True

    except Exception as e:
        print(f"\nError: {e}")
        return False