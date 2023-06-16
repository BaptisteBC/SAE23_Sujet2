CREATE database sae23_sujet2;

USE sae23_sujet2;

CREATE TABLE `filmographie_personne` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `pseudo` varchar(255) NOT NULL,
  `nom` varchar(255) NOT NULL,
  `prenom` varchar(255) NOT NULL,
  `mail` varchar(255) NOT NULL,
  `mot_de_passe` varchar(255) NOT NULL,
  `type` varchar(13) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `pseudo` (`pseudo`)
);

CREATE TABLE `filmographie_acteur` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  `prenom` varchar(255) DEFAULT NULL,
  `age` int DEFAULT NULL,
  `photos` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
);

CREATE TABLE `filmographie_categorie` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `nom` varchar(255) NOT NULL,
  `descriptif` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nom` (`nom`)
);

CREATE TABLE `filmographie_commentaire` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `note` int NOT NULL,
  `commentaire` longtext NOT NULL,
  `date` date NOT NULL,
  `film_id` bigint NOT NULL,
  `personne_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `filmographie_comment_film_id_55ff8448_fk_filmograp` (`film_id`),
  KEY `filmographie_comment_personne_id_3e4d2d5c_fk_filmograp` (`personne_id`),
  CONSTRAINT `filmographie_comment_film_id_55ff8448_fk_filmograp` FOREIGN KEY (`film_id`) REFERENCES `filmographie_film` (`id`),
  CONSTRAINT `filmographie_comment_personne_id_3e4d2d5c_fk_filmograp` FOREIGN KEY (`personne_id`) REFERENCES `filmographie_personne` (`id`)
);

CREATE TABLE `filmographie_film` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `titre` varchar(255) NOT NULL,
  `annee_sortie` int NOT NULL,
  `affiche` varchar(100) DEFAULT NULL,
  `realisateur` varchar(255) NOT NULL,
  `categorie_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `titre` (`titre`),
  KEY `filmographie_film_categorie_id_62de48a2_fk_filmograp` (`categorie_id`),
  CONSTRAINT `filmographie_film_categorie_id_62de48a2_fk_filmograp` FOREIGN KEY (`categorie_id`) REFERENCES `filmographie_categorie` (`id`)
);

CREATE TABLE `filmographie_film_acteur` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `acteur_id` bigint NOT NULL,
  `film_id` bigint NOT NULL,
  PRIMARY KEY (`id`),
  KEY `filmographie_film_ac_acteur_id_e75ea965_fk_filmograp` (`acteur_id`),
  KEY `filmographie_film_ac_film_id_02ffa3fa_fk_filmograp` (`film_id`),
  CONSTRAINT `filmographie_film_ac_acteur_id_e75ea965_fk_filmograp` FOREIGN KEY (`acteur_id`) REFERENCES `filmographie_acteur` (`id`),
  CONSTRAINT `filmographie_film_ac_film_id_02ffa3fa_fk_filmograp` FOREIGN KEY (`film_id`) REFERENCES `filmographie_film` (`id`)
);
