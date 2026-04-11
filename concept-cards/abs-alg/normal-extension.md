---
concept: Normal Extension
slug: normal-extension
category: field-theory
subcategory: splitting-fields
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Galois Theory"
chapter_number: 14
pdf_page: 558
section: "14.1 Basic Definitions"
extraction_confidence: high
aliases: []
prerequisites:
  - field-extension
  - splitting-field
extends: []
related:
  - galois-extension
  - separable-extension
contrasts_with:
  - separable-extension
answers_questions:
  - "What is a normal extension?"
  - "What distinguishes a normal extension from a separable extension?"
---

# Quick Definition
A finite extension K/F is normal if K is the splitting field of some polynomial over F. Equivalently, every irreducible polynomial in F[x] that has one root in K splits completely in K.

# Core Definition
A finite extension K/F is normal if every irreducible polynomial in F[x] that has a root in K splits completely over K. Equivalently, K is the splitting field of some (not necessarily irreducible) polynomial $f(x) \in F[x]$. K/F is Galois iff it is both normal and separable (Dummit & Foote, pp. 558-561, 537-538).

# Prerequisites
- **field-extension** — Normal is a property of extensions
- **splitting-field** — Normal extensions are splitting fields

# Key Properties
1. Normal $\iff$ splitting field of some polynomial
2. If $\alpha \in K$ has minimal polynomial $m(x)$ over F, and K/F is normal, then $m(x)$ splits in K
3. Galois = normal + separable
4. Over characteristic 0: Galois $\iff$ normal
5. Normal extensions of normal extensions need not be normal (normality is NOT transitive)

# Relationships
## Builds Upon
- **field-extension**, **splitting-field**

## Enables
- **galois-extension** — Galois = normal + separable

## Contrasts With
- **separable-extension** — Separability concerns repeated roots; normality concerns completeness of splitting

# Common Confusions
- **Confusion**: Thinking normality is transitive. **Clarification**: $\mathbb{Q} \subset \mathbb{Q}(\sqrt{2}) \subset \mathbb{Q}(\sqrt[4]{2})$ where each step is normal (degree 2) but $\mathbb{Q}(\sqrt[4]{2})/\mathbb{Q}$ is not normal.

# Source Reference
Chapter 13, Section 13.4 and Chapter 14, Section 14.1.

# Verification Notes
- Confidence: HIGH — explicit definition
