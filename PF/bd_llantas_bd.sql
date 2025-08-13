-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 13-08-2025 a las 04:56:33
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_llantas`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `llantas`
--
create data base if not exists bd_llantas;

CREATE TABLE `llantas` (
  `id` int(11) NOT NULL,
  `marca` varchar(50) DEFAULT NULL,
  `categoria` varchar(50) DEFAULT NULL,
  `medida` varchar(50) DEFAULT NULL,
  `estado` varchar(50) DEFAULT NULL,
  `precio` decimal(10,2) DEFAULT NULL,
  `cantidad` int(11) DEFAULT NULL,
  `usuario_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `llantas`
--

INSERT INTO `llantas` (`id`, `marca`, `categoria`, `medida`, `estado`, `precio`, `cantidad`, `usuario_id`) VALUES
(6, 'a', 'a', 'a', 'a', 12.00, 6, 1),
(7, 'michelin', '1234', '12', '12', 12.00, 0, 1),
(8, 'Michelin', 'T/M', '333/77/65', 'Usada', 300.00, 28, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `registro_ventas`
--

CREATE TABLE `registro_ventas` (
  `id` int(11) NOT NULL,
  `llanta_id` int(11) NOT NULL,
  `usuario_id` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `total` decimal(10,2) NOT NULL,
  `fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `registro_ventas`
--

INSERT INTO `registro_ventas` (`id`, `llanta_id`, `usuario_id`, `cantidad`, `total`, `fecha`) VALUES
(3, 7, 1, 12, 144.00, '2025-08-11'),
(4, 6, 1, 6, 72.00, '2025-08-12');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id` int(11) NOT NULL,
  `nombre` varchar(70) NOT NULL,
  `apellidos` varchar(70) NOT NULL,
  `correo` varchar(70) NOT NULL,
  `password` varchar(100) NOT NULL,
  `fecha` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id`, `nombre`, `apellidos`, `correo`, `password`, `fecha`) VALUES
(1, 'danna', 'alvarado', 'danna@gmail,com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', '2025-08-11'),
(2, 'a', 'a', 'a', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', '2025-08-11'),
(3, 'er', 'er', 'erf', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', '2025-08-11'),
(5, 'miguel', 'medina', 'miguel@gmail.com', 'a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3', '2025-08-12');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `llantas`
--
ALTER TABLE `llantas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_llantas_usuarios` (`usuario_id`);

--
-- Indices de la tabla `registro_ventas`
--
ALTER TABLE `registro_ventas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `fk_ventas_llantas` (`llanta_id`),
  ADD KEY `fk_ventas_usuarios` (`usuario_id`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `llantas`
--
ALTER TABLE `llantas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `registro_ventas`
--
ALTER TABLE `registro_ventas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `llantas`
--
ALTER TABLE `llantas`
  ADD CONSTRAINT `fk_llantas_usuarios` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `registro_ventas`
--
ALTER TABLE `registro_ventas`
  ADD CONSTRAINT `fk_ventas_llantas` FOREIGN KEY (`llanta_id`) REFERENCES `llantas` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_ventas_usuarios` FOREIGN KEY (`usuario_id`) REFERENCES `usuarios` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
