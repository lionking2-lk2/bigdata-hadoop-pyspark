# 🚀 Big Data Project - Hadoop & PySpark

## 📌 Description du projet

Ce projet est une simulation complète d’un pipeline **Big Data** utilisant :

- Python (génération de données)
- Hadoop HDFS (stockage distribué)
- PySpark (traitement des données)
- Analyse métier (Business Intelligence)

L’objectif est de simuler un système de transactions (type e-commerce ou banque), puis de :
- stocker les données dans HDFS
- nettoyer les données avec Spark
- calculer des indicateurs métier
- analyser les performances

---

## 🏗️ Architecture du projet


BigData-Hadoop-PySpark/
│
├── fictif.py → Génération de données fictives (utilisateurs/transactions)
├── transaction.py → Création du dataset de transactions
├── pyhdfs.py → Gestion et envoi des données vers HDFS
├── spark.py → Pipeline Spark (lecture + traitement)
├── analys.py → Analyse métier (KPI, chiffre d’affaires, etc.)
├── count.py → Calcul du nombre total de transactions
├── count10.py → Tests de performance et comparaison de lecture


---

## ⚙️ Fonctionnalités

### 📊 Génération de données
- Création de données fictives avec Python
- Simulation de transactions réalistes
- Génération de milliers à millions de lignes

---

### 📦 Stockage HDFS
- Envoi des fichiers vers Hadoop HDFS
- Gestion du stockage distribué

---

### ⚡ Traitement avec PySpark
- Lecture des données depuis HDFS
- Nettoyage des données
- Transformation et préparation des datasets

---

### 📈 Analyse métier (BI)
- Chiffre d’affaires total
- Produits les plus vendus
- Analyse des villes les plus actives
- Taux de réussite des transactions

---

### 🧪 Tests & performance
- Comptage des données (`count.py`)
- Comparaison de performance de lecture (`count10.py`)

---

## 📊 Exemples de KPI calculés

- 💰 Chiffre d’affaires total
- 📦 Top produits vendus
- 🏙️ Ville la plus active
- ✅ Taux de réussite des transactions
- ❌ Taux d’échec

---

## 🛠️ Technologies utilisées

- Python 🐍
- Apache Hadoop (HDFS) 📦
- Apache Spark ⚡
- PySpark 🔥
- Git & GitHub 🌐

---

## 🎯 Objectif pédagogique

Ce projet permet de comprendre :

- Le fonctionnement d’un pipeline Big Data
- Le stockage distribué avec HDFS
- Le traitement distribué avec Spark
- Les bases de l’analyse de données (BI)

---

## 👨‍💻 Auteur

Projet réalisé dans un but d’apprentissage du Big Data et de l’ingénierie des données.

---

## 🚀 Améliorations possibles

- Optimisation Spark (Parquet, partitionnement)
- Ajout de Machine Learning
- Création de dashboards (Power BI / Streamlit)
- Automatisation du pipeline (Airflow)
```
