---
concept: Sylow p-Subgroup
slug: sylow-p-subgroup
category: group-structure
subcategory: sylow-theory
tier: advanced
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "The Sylow Theorems"
chapter_number: 15
pdf_page: 196
section: "The Sylow Theorems"
extraction_confidence: high
aliases:
  - "Sylow subgroup"
  - "maximal p-subgroup"
prerequisites:
  - p-subgroup
  - first-sylow-theorem
extends:
  - p-subgroup
related:
  - normalizer
  - second-sylow-theorem
  - third-sylow-theorem
contrasts_with:
  - p-subgroup
answers_questions:
  - "What is a Sylow p-subgroup?"
  - "How do I use the Sylow theorems to analyze group structure?"
---

# Quick Definition

A Sylow $p$-subgroup of $G$ is a maximal $p$-subgroup, i.e., a $p$-subgroup not properly contained in any other $p$-subgroup. If $|G| = p^n m$ with $\gcd(p, m) = 1$, then a Sylow $p$-subgroup has order $p^n$.

# Core Definition

"A **Sylow $p$-subgroup** $P$ of a group $G$ is a maximal $p$-subgroup of $G$" (Judson, p. 196). If $|G| = p^n m$ where $p \nmid m$, then $|P| = p^n$.

# Prerequisites

- **$p$-subgroup** — A Sylow $p$-subgroup is a maximal one
- **First Sylow theorem** — Guarantees existence

# Key Properties

1. Exists for every prime $p$ dividing $|G|$ (First Sylow Theorem)
2. All Sylow $p$-subgroups are conjugate (Second Sylow Theorem)
3. The number of Sylow $p$-subgroups divides $|G|$ and is $\equiv 1 \pmod{p}$ (Third Sylow Theorem)
4. A Sylow $p$-subgroup is normal iff it is the unique Sylow $p$-subgroup
5. If $P$ is a Sylow $p$-subgroup and $x$ has $p$-power order with $x^{-1}Px = P$, then $x \in P$ (Lemma 15.5)

# Context & Application

Sylow $p$-subgroups are the primary tool for analyzing the structure of finite groups. By determining the number and structure of Sylow subgroups, one can often classify groups of a given order or prove that a group is not simple.

# Examples

**Example 1** (p. 198): For $A_5$ ($|A_5| = 60 = 2^2 \cdot 3 \cdot 5$):
- Sylow 5-subgroups have order 5; there are exactly 6
- Sylow 3-subgroups have order 3
- Sylow 2-subgroups have order 4

# Relationships

## Builds Upon
- **$p$-subgroup** — Sylow $p$-subgroups are maximal

## Enables
- **Group classification** — Central tool for classifying finite groups
- **Proving non-simplicity** — A unique Sylow $p$-subgroup is normal

## Contrasts With
- **$p$-subgroup** — Not every $p$-subgroup is a Sylow $p$-subgroup (only maximal ones)

# Source Reference

Chapter 15: The Sylow Theorems, Section 15.1, p. 196.

# Verification Notes

- Definition source: Direct from p. 196
- Confidence: HIGH
