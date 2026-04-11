---
concept: Annihilator
slug: annihilator
category: ring-theory
subcategory: ideals
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 250
section: "7.3 Ring Homomorphisms and Quotient Rings"
extraction_confidence: high
aliases:
  - "left annihilator"
  - "right annihilator"
prerequisites:
  - ring
  - ideal
extends: []
related:
  - zero-divisor
contrasts_with: []
answers_questions:
  - "What is the annihilator of an element in a ring?"
---

# Quick Definition
The right annihilator of $a \in R$ is $\{x \in R \mid ax = 0\}$ (a right ideal); the left annihilator is $\{y \in R \mid ya = 0\}$ (a left ideal).

# Core Definition
Let $a \in R$. The set $\{x \in R \mid ax = 0\}$ is a right ideal (the *right annihilator* of a) and $\{y \in R \mid ya = 0\}$ is a left ideal (the *left annihilator* of a). The left annihilator of a left ideal L is a two-sided ideal (Exercise 22, Dummit & Foote, p. 250).

# Prerequisites
- **Ring** — Annihilators are defined in rings
- **Ideal** — Annihilators are ideals

# Key Properties
1. Right annihilator of a is a right ideal
2. Left annihilator of a is a left ideal
3. Left annihilator of a left ideal is a two-sided ideal
4. $a$ is a zero divisor iff its annihilator is nontrivial

# Source Reference
Chapter 7, Section 7.3, Exercise 22, page 250.

# Verification Notes
- Definition: From Exercise 22, p. 250
- Confidence: HIGH — explicit definition in exercises
