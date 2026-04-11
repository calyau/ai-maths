---
concept: "Burnside's Lemma (Counting)"
slug: burnsides-lemma
category: representation-theory
subcategory: applications
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Examples and Applications of Character Theory"
chapter_number: 19
pdf_page: 880
section: "19.1 Characters of Groups of Small Order"
extraction_confidence: medium
aliases:
  - "Cauchy-Frobenius lemma"
prerequisites:
  - group
extends: []
related: []
contrasts_with: []
answers_questions:
  - "What is Burnside's counting lemma?"
---

# Quick Definition
The number of orbits of a finite group G acting on a set X equals (1/|G|)Σ_{g∈G}|X^g|, the average number of fixed points.

# Core Definition
**Burnside's Lemma** (Counting Formula): For a finite group G acting on a finite set X, the number of orbits equals (1/|G|)Σ_{g∈G}|X^g| where X^g = {x ∈ X | gx = x} is the set of fixed points of g. This is used in conjunction with character theory in Chapter 19.

# Prerequisites
- **group** — G acts on a set

# Source Reference
Chapter 19, referenced in applications, pages 880-892.

# Verification Notes
- Confidence: MEDIUM — referenced but not the primary focus
