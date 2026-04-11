---
concept: Galois Group
slug: galois-group
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
  - "Gal(K/F)"
prerequisites:
  - galois-extension
  - field-automorphism
extends: []
related:
  - fundamental-theorem-galois-theory
  - fixed-field
contrasts_with: []
answers_questions:
  - "What is the Galois group?"
---

# Quick Definition
The Galois group $\text{Gal}(K/F)$ of a Galois extension K/F is the group of all field automorphisms of K that fix F pointwise. Its order equals $[K:F]$.

# Core Definition
If K/F is a Galois extension, the Galois group $\text{Gal}(K/F) = \text{Aut}(K/F) = \{\sigma: K \to K \mid \sigma \text{ is a field automorphism with } \sigma(a) = a \text{ for all } a \in F\}$. This is a group under composition with $|\text{Gal}(K/F)| = [K:F]$. Elements of the Galois group permute the roots of any polynomial over F (Dummit & Foote, pp. 558-561).

# Prerequisites
- **galois-extension** — The Galois group is defined for Galois extensions
- **field-automorphism** — Elements are field automorphisms fixing F

# Key Properties
1. $|\text{Gal}(K/F)| = [K:F]$
2. Automorphisms permute roots of irreducible polynomials over F
3. The Galois group acts faithfully on the roots of any generating polynomial
4. For the splitting field of $f(x)$, $\text{Gal}(K/F)$ embeds in $S_n$ (n = deg f)
5. The fixed field $K^{\text{Gal}(K/F)} = F$

# Context & Application
The Galois group encodes all the symmetries of a field extension. Computing it is a central problem: for specific polynomials, techniques include examining degrees, discriminants, resolvents, and reduction modulo primes.

# Examples
**Example 1** (p. 562): $\text{Gal}(\mathbb{Q}(\sqrt{2})/\mathbb{Q}) \cong \mathbb{Z}/2\mathbb{Z}$ (swap $\sqrt{2} \leftrightarrow -\sqrt{2}$).
**Example 2** (p. 563): $\text{Gal}(\mathbb{Q}(\zeta_p)/\mathbb{Q}) \cong (\mathbb{Z}/p\mathbb{Z})^{\times}$ for a pth root of unity $\zeta_p$.

# Relationships
## Builds Upon
- **galois-extension**

## Enables
- **fundamental-theorem-galois-theory** — Connects subgroups to intermediate fields

# Source Reference
Chapter 14, Section 14.1, pp. 558-569.

# Verification Notes
- Confidence: HIGH — central definition
