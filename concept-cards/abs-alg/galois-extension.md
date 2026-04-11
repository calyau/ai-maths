---
concept: Galois Extension
slug: galois-extension
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
  - "Galois field extension"
prerequisites:
  - field-extension
  - separable-extension
  - normal-extension
  - splitting-field
extends: []
related:
  - galois-group
  - fundamental-theorem-galois-theory
  - fixed-field
contrasts_with: []
answers_questions:
  - "What is a Galois extension?"
  - "What must I know before studying Galois theory?"
---

# Quick Definition
A finite extension K/F is Galois if it is both normal and separable, equivalently if K is the splitting field of a separable polynomial over F, equivalently if $|\text{Aut}(K/F)| = [K:F]$.

# Core Definition
A finite extension K/F is called a Galois extension if $|\text{Aut}(K/F)| = [K:F]$. Equivalently, K/F is Galois iff it is both separable and normal, iff K is the splitting field of some separable polynomial over F, iff the fixed field of $\text{Aut}(K/F)$ is exactly F. The group $\text{Aut}(K/F)$ is then called the Galois group of K/F, denoted $\text{Gal}(K/F)$ (Dummit & Foote, pp. 558-569).

# Prerequisites
- **field-extension** — Galois extensions are field extensions
- **separable-extension** — Galois implies separable
- **normal-extension** — Galois implies normal
- **splitting-field** — Galois extensions are splitting fields of separable polynomials

# Key Properties
1. K/F Galois $\iff$ separable + normal $\iff$ splitting field of separable polynomial
2. $|\text{Gal}(K/F)| = [K:F]$
3. The fixed field of $\text{Gal}(K/F)$ is F
4. For $\sigma \in \text{Gal}(K/F)$, $\sigma$ permutes the roots of any irreducible polynomial over F
5. Over $\mathbb{Q}$ (or any characteristic 0 field), Galois $\iff$ normal $\iff$ splitting field

# Construction / Recognition
## To Verify K/F is Galois:
1. Check K is a splitting field of some polynomial $f(x) \in F[x]$, AND
2. Check f(x) is separable (automatic in characteristic 0)

OR: Check $|\text{Aut}(K/F)| = [K:F]$

# Context & Application
Galois extensions are the "right" extensions for Galois theory. The fundamental theorem establishes a correspondence between intermediate fields and subgroups of the Galois group.

# Examples
**Example 1** (p. 561): $\mathbb{Q}(\sqrt{2})/\mathbb{Q}$ is Galois; $\text{Gal} \cong \mathbb{Z}/2\mathbb{Z}$.
**Example 2** (p. 563): $\mathbb{Q}(\sqrt[3]{2})/\mathbb{Q}$ is NOT Galois (not normal; $x^3 - 2$ doesn't split).

# Relationships
## Builds Upon
- **field-extension**, **separable-extension**, **normal-extension**, **splitting-field**

## Enables
- **galois-group** — The automorphism group of a Galois extension
- **fundamental-theorem-galois-theory** — The main theorem connecting subgroups and subfields

# Source Reference
Chapter 14, Section 14.1, pp. 558-569.

# Verification Notes
- Confidence: HIGH — central definition of the chapter
