---
concept: Fixed Field
slug: fixed-field
category: galois-theory
subcategory: basic-definitions
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Galois Theory"
chapter_number: 14
pdf_page: 558
section: "14.1 Basic Definitions"
extraction_confidence: high
aliases:
  - "field of invariants"
prerequisites:
  - field-extension
  - galois-group
extends: []
related:
  - fundamental-theorem-galois-theory
contrasts_with: []
answers_questions:
  - "What is a fixed field?"
---

# Quick Definition
The fixed field of a group H of automorphisms of K is $K^H = \{a \in K \mid \sigma(a) = a \text{ for all } \sigma \in H\}$. It is the subfield of elements left unchanged by all automorphisms in H.

# Core Definition
If H is a subgroup of $\text{Aut}(K)$, the fixed field $K^H = \{a \in K \mid \sigma(a) = a \text{ for all } \sigma \in H\}$ is a subfield of K. By the fundamental theorem, if K/F is Galois, then $K^{\text{Gal}(K/F)} = F$ and the map $H \mapsto K^H$ gives one direction of the Galois correspondence (Dummit & Foote, pp. 558-560).

# Prerequisites
- **field-extension**, **galois-group**

# Key Properties
1. $K^H$ is always a subfield of K
2. $[K:K^H] = |H|$ when H is finite
3. $K^{\text{Gal}(K/F)} = F$ for Galois extensions
4. The map $H \mapsto K^H$ and $E \mapsto \text{Gal}(K/E)$ are inverse bijections

# Relationships
## Builds Upon
- **field-extension**, **galois-group**

## Enables
- **fundamental-theorem-galois-theory**

# Source Reference
Chapter 14, Section 14.1, pp. 558-561.

# Verification Notes
- Confidence: HIGH — explicit definition
