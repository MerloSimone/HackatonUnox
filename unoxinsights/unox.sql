-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: localhost    Database: unox
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `messages`
--

DROP TABLE IF EXISTS `messages`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `messages` (
  `id_message` int NOT NULL AUTO_INCREMENT,
  `user_message` varchar(2000) DEFAULT NULL,
  `generated_response` varchar(2000) DEFAULT NULL,
  `datetime` datetime NOT NULL,
  `summary` varchar(2000) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `category` varchar(100) DEFAULT NULL,
  `id_user` int NOT NULL,
  PRIMARY KEY (`id_message`),
  KEY `id_user` (`id_user`),
  CONSTRAINT `messages_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `users` (`id_user`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `messages`
--

LOCK TABLES `messages` WRITE;
/*!40000 ALTER TABLE `messages` DISABLE KEYS */;
INSERT INTO `messages` VALUES (1,'sdsadafdsf\r\n','Thank you for contacting us. I apologize you are having trouble finding a solution. Could you please provide some additional details on what you are trying to accomplish? Providing more context will help me better assist you in finding a solution.','2024-03-10 02:14:59','Technical Support','The user is having difficulty finding a solution and has provided limited context.',2),(2,'Ciao carissimo\r\n','Dear customer, thank you for contacting us. I\'m afraid your email does not contain enough information for me to provide a specific response. Please let me know how I can assist you or what questions you have, and I\'ll be happy to help. Looking forward to hearing from you.','2024-03-10 03:17:29','General Inquiry','The email contains a general greeting but does not include any specific request or information.',2),(3,'Unox ovens are the best\r\n','Thank you for your email. Unox ovens are high-quality professional ovens that many chefs and bakers prefer for their reliability, consistent baking results, and innovative features. However, there are other excellent oven brands on the market that may also meet your needs. I\'d be happy to discuss Unox ovens and other options in more detail to help you find the best oven for your requirements.','2024-03-10 04:11:52','Product information','The email is asking if Unox ovens are the best ovens available.',2),(4,'Ciao unox\r\n','Dear customer, I apologize you are unable to find the answer to your question in the document provided. I would be happy to assist in answering your question or providing any clarification needed. Please let me know the specifics of what you are looking for, and I will do my best to find the answer for you or point you in the right direction.','2024-03-10 04:33:07','Technical Support','The user is unable to find the answer to their question in a provided document and is reaching out f',2),(5,'Ciao unox\r\n','Dear customer, I apologize but the information you are requesting is not contained in the document provided. Please let me know if you have any other questions I can assist with. Have a great day!','2024-03-10 04:35:16','General Inquiry','The email asks for information that is not present in the provided document. It signs off with \'Ciao',2),(6,'prova\r\n','The UNOX oven\'s ADAPTIVE.Cooking system automatically adjusts cooking time, temperature, and humidity to ensure consistent results every time. This innovative technology monitors factors like ingredient size and quantity in real-time, adapting the cooking process for reliable, high-quality output without the need for manual adjustment.','2024-03-10 04:50:32','Product information','The email is asking about features of the UNOX oven, specifically the ADAPTIVE.Cooking system.',2),(7,'ciao\r\n','Thank you for your interest in the Unox Intensive Cooking combi oven. This is an advanced combi oven designed for gastronomy cooking. Key features include rapid humidity extraction, increased steam saturation, automatic fan speed and direction control, data-driven cooking apps, smoker box accessory, water connections, Ethernet connectivity, stainless steel cooking chamber, triple glass door, integrated detergent container and drain valve, and WiFi connectivity for HACCP data transfer. Please let me know if you need any other details or have additional questions about this combi oven model and its capabilities.','2024-03-10 05:13:29','General Inquiry','The email is asking for general information about the features and specifications of the Unox Intens',2),(8,'Tell me about cheftop-x oven\r\n','Thank you for your inquiry about the CHEFTOP MIND.Maps PLUS oven. This is a top-of-the-line combi oven from Unox that offers a wide variety of cooking methods including steaming, sous vide, roasting, grilling, and more. It features innovative technologies like Unox Intensive Cooking and Intelligence Performance to ensure perfect results every time, regardless of load size. The oven can even automate cooking with the CHEFUNOX program, making it easy to achieve consistent outcomes without needing trained staff. Some key features include dehydrating, low temperature cooking, plate regeneration, and repeatability for high volume operations. Please let me know if you need any other details on this advanced combi oven solution.','2024-03-10 08:14:18','Product Information','The email is asking for information about the CHEFTOP MIND.Maps PLUS oven, which is a technologicall',2),(9,'water is leaking from the oven, what can I do?\r\n','I\'m sorry to hear you are having issues with water leaking from your oven. As a first step, I recommend consulting your oven\'s user manual for troubleshooting tips. If you don\'t have the manual, you can try contacting the manufacturer directly for advice and assistance with resolving the leak.','2024-03-10 08:32:02','Technical Support','The email is reporting that water is leaking from their oven and asking what they can do about it.',10),(10,'water is leaking from the oven, what can I do?\r\n','I apologize for the issue you are having with your oven leaking water. Here are some tips that may help resolve this:\n\n- Make sure the oven is level. An unleveled oven can cause water to pool and leak out. You can adjust the leveling legs underneath to make it level.\n\n- Check the water reservoir and steam vent. Overflow or clogs in these areas can lead to water spilling into the oven. Clean out any debris and make sure the water reservoir is not overfilled. \n\n- Inspect the oven door seal. A damaged or worn seal will allow steam and moisture to escape from the oven cavity. The seal may need to be replaced.\n\n- Try running a self-cleaning cycle which can help dry out any excess water buildup inside the oven. \n\nIf none of these tips resolve your issue, I recommend having a technician inspect the oven for any other leaks or part failures. Please let me know if you need help arranging a service appointment. I\'m happy to assist further in getting this taken care of.','2024-03-10 08:35:32','Technical Support','Customer is experiencing a water leak from their oven and is asking for help troubleshooting the iss',10),(11,'Tell me about cheftop-x oven\r\n','Thank you for your interest in the cheftop-x oven. The cheftop-x is our newest model convection oven, featuring 5 cooking modes, a large 5 cubic foot interior, and a smooth glass touchscreen control panel. It reaches temperatures up to 500°F and the convection fan allows for fast, even cooking. Some key features include a built-in temperature probe, timed cooking, and adjustable racks. Please let me know if you have any other questions!','2024-03-10 10:04:42','Product information','The user is asking for information about the cheftop-x oven.',12),(12,'water is leaking from the oven, what can I do?\r\n','I apologize for the issue you are having with your oven leaking water. Here are some tips that may help resolve this:\n\n- Make sure the oven is level. An unleveled oven can cause water to pool and leak out. You can adjust the leveling legs underneath the oven to make it level.\n\n- Check the water reservoir and steam vent. Overflow or clogs in these areas can lead to water spilling into the oven. Clean out any debris and make sure the water reservoir is not overfilled. \n\n- Inspect the oven door seal. A damaged or worn seal will allow steam and moisture to escape from the oven cavity. The seal may need to be replaced.\n\n- Try running a self-clean cycle which will dry out any moisture buildup inside the oven. \n\nIf none of these tips resolve your issue, I recommend having a technician inspect the oven for any other leaks or part failures. Please let me know if you need help arranging a service appointment. I\'m happy to assist further in getting this taken care of.\n\n','2024-03-10 10:34:21','Technical Support','Customer is experiencing a water leak from their oven and is asking for help troubleshooting the iss',10);
/*!40000 ALTER TABLE `messages` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id_user` int NOT NULL AUTO_INCREMENT,
  `email_address` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id_user`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'aaaa@bbbb.com'),(2,'MCazzaro@izsvenezie.it'),(3,'MCazzaro@izsvenezie.it'),(4,'MCazzaro@izsvenezie.it'),(5,'MCazzaro@izsvenezie.it'),(6,'MCazzaro@izsvenezie.it'),(7,'MCazzaro@izsvenezie.it'),(8,'MCazzaro@izsvenezie.it'),(9,'MCazzaro@izsvenezie.it'),(10,'simone.merlo00@gmail.com'),(11,'simone.merlo00@gmail.com'),(12,'mirco.cazzaro.1999@gmail.com'),(13,'simone.merlo00@gmail.com');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-11 11:36:43
