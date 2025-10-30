# Mémoire M2 : Processus de Poisson Modulé par Chaîne de Markov (MMPP)

**Auteur** : Kouassi Innocent N'GORAN  
**Encadreur** : [Nom]  
**Date** : Octobre 2025

---

## Objectif

Ce dépôt contient **tous les codes Python** utilisés dans le mémoire de Master 2 :

> **"Processus de Poisson Modulé par Chaîne de Markov : Modélisation, propriétés fondamentales et perspectives d'application"**

Les codes sont **exécutables**, **commentés**, et **reproduisent les résultats du mémoire**.

---

## Structure du dépôt

| Fichier | Description |
|--------|-------------|
| `mmpp_simulation.py` | Simulation et validation d’un MMPP à 2 états (F(∞), p, F(t)) |
| `ipp_simulation.py` | Simulation IPP + lien avec la loi hyperexponentielle H₂ |
| `superposition.py` | Superposition de 2 MMPP via somme de Kronecker + norme L² |
| `covid_mmp_em.py` | Modélisation COVID-19 (mars 2020) avec EM à 3 régimes |
- `A5_interarrivals_regimes.py` : Validation des temps inter-arrivées par régime (COVID-19)
- `A6_hft_analysis.py` : Analyse exploratoire des données HFT Bitcoin
- `A7_cyber_superposition.py` : Validation graphique de la superposition MMPP (cybersécurité)
---

## Installation

```bash
git clone https://github.com/ton-pseudo/memoire-m2-mmpp.git
cd memoire-m2-mmpp
pip install -r requirements.txt
