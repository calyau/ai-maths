---
# === CORE IDENTIFICATION ===
concept: Word Problem
slug: word-problem

# === CLASSIFICATION ===
category: free-groups-presentations
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Free Groups and Presentations; Coxeter Groups"
chapter_number: 2
pdf_page: 37
section: "Finitely presented groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - word problem for groups

# === TYPED RELATIONSHIPS ===
prerequisites:
  - finitely-presented-group
extends: []
related:
  - burnside-problem
  - todd-coxeter-algorithm
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the word problem for groups?"
  - "Is it always possible to decide if a word represents the identity?"
---

# Quick Definition

The word problem for a finitely presented group $G = \langle X \mid R \rangle$ asks: is there an algorithm to decide whether a given word on $X'$ represents the identity element in $G$?

# Core Definition

"The word problem for $G$ asks whether there exists an algorithm (decision procedure) for deciding whether a word on $X'$ represents 1 in $G$. The answer is negative: Novikov and Boone showed that there exist finitely presented groups $G$ for which no such algorithm exists." (Milne, p. 37)

# Prerequisites

- **Finitely presented group** — the word problem is posed for such groups

# Key Properties

1. There exist finitely presented groups with unsolvable word problem (Novikov-Boone)
2. Many specific groups do have solvable word problems (e.g., free groups, Coxeter groups)
3. Related undecidable problems: determining if a presentation gives the trivial group, a finite group, an abelian group, a solvable group, etc.

# Context & Application

The word problem is one of the fundamental decision problems in combinatorial group theory. Its unsolvability shows the inherent difficulty of working with group presentations. Specific algorithms (like Todd-Coxeter) can still solve instances.

# Examples

**Example 1** (p. 37): There is no algorithm to determine for an arbitrary finite presentation whether the group is trivial, finite, abelian, solvable, nilpotent, simple, torsion, torsion-free, free, or has a solvable word problem.

# Relationships

## Builds Upon
- **finitely-presented-group**

## Related
- **burnside-problem** — another fundamental decision problem
- **todd-coxeter-algorithm** — a practical tool for specific instances

# Source Reference

Chapter 2, Section "The word problem", page 37. References: Rotman 1995, Chapter 12.

# Verification Notes

- Definition source: Direct from p. 37
- Confidence: HIGH
- Uncertainties: None
