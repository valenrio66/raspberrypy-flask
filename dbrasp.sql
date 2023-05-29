-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 29, 2023 at 09:15 AM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbrasp`
--

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id_user` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `salt` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id_user`, `username`, `password`, `salt`) VALUES
(43, 'valen', '$2b$12$MtgGbzqGM8IAIXLqU2wfG.2xvSCZy85MXfpNiiCuYnQsfe6BpeHBe', '$2b$12$MtgGbzqGM8IAIXLqU2wfG.'),
(44, 'richard', '$2b$12$tqHFnvSdnUEoUhq7slXcjOri72aiWLyZKylcphyc3TA4LCH85jgne', '$2b$12$tqHFnvSdnUEoUhq7slXcjO'),
(45, 'wayne', '$2b$12$KuY8a3X.RgI2HGlQCKe.6.u28chq2fZ7LpyDm3x5Vbh/nIAjO6PTW', '$2b$12$KuY8a3X.RgI2HGlQCKe.6.'),
(46, 'testingbrow', '$2b$12$UFClERA6A9RGdASvgc..COrOPnHqpnX6S1R4BGK3Kzp/wl0kGTtvS', '$2b$12$UFClERA6A9RGdASvgc..CO'),
(47, 'riorio', '$2b$12$PUgD4wnC4sj0ddpwaOK4JuFincxQ4y0ENns81psEwY4WPXamo4RLS', '$2b$12$PUgD4wnC4sj0ddpwaOK4Ju');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id_user`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id_user` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=48;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
