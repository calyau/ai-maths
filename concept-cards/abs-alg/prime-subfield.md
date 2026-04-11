---
concept: Prime Subfield
slug: prime-subfield
category: ring-theory
subcategory: basic-definitions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 265
section: "7.5 Rings of Fractions"
extraction_confidence: high
aliases: []
prerequisites:
  - field
  - characteristic-of-ring
extends: []
related:
  - field
contrasts_with: []
answers_questions:
  - "What is the prime subfield of a field?"
---

# Quick Definition
Every field F contains a unique smallest subfield $F_0$ (the prime subfield), isomorphic to $\mathbb{Q}$ if $\text{char}(F) = 0$ or to $\mathbb{Z}/p\mathbb{Z}$ if $\text{char}(F) = p$.

# Core Definition
Every field F contains a unique smallest subfield $F_0$, called the *prime subfield* of F. It is isomorphic to $\mathbb{Q}$ if $\text{char}(F) = 0$ or to $\mathbb{Z}/p\mathbb{Z}$ if $\text{char}(F) = p$ (Exercise 3, Dummit & Foote, p. 265).

# Prerequisites
- **Field** — The prime subfield lives inside a field
- **Characteristic** — Determines which prime subfield

# Key Properties
1. Any subfield of $\mathbb{R}$ contains $\mathbb{Q}$ (Exercise 4, p. 265)
2. The prime subfield is the image of the canonical map $\mathbb{Z} \to F$ followed by taking the field of fractions

# Source Reference
Chapter 7, Section 7.5, Exercise 3, page 265.

# Verification Notes
- Definition: From Exercise 3, p. 265
- Confidence: HIGH — standard result
