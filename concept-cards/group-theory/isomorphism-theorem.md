---
# === CORE IDENTIFICATION ===
concept: Isomorphism Theorem
slug: isomorphism-theorem

# === CLASSIFICATION ===
category: homomorphisms
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 22
section: "Theorems concerning homomorphisms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - second isomorphism theorem
  - diamond isomorphism theorem

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normal-subgroup
  - quotient-group
  - factorization-theorem
extends: []
related:
  - correspondence-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are H/(H cap N) and HN/N related?"
  - "What is the second isomorphism theorem?"
---

# Quick Definition

If $H \le G$ and $N \trianglelefteq G$, then $HN$ is a subgroup, $H \cap N \trianglelefteq H$, and $H/(H \cap N) \cong HN/N$.

# Core Definition

"Let $H$ be a subgroup of $G$ and $N$ a normal subgroup of $G$. Then $HN$ is a subgroup of $G$, $H \cap N$ is a normal subgroup of $H$, and the map $h(H \cap N) \mapsto hN: H/H \cap N \to HN/N$ is an isomorphism." (Milne, Theorem 1.46, p. 22)

# Prerequisites

- **Normal subgroup** — $N$ must be normal in $G$
- **Quotient group** — both sides involve quotients
- **Factorization theorem** — the proof applies it to $H \to G/N$

# Key Properties

1. $HN$ is a subgroup of $G$ (by Proposition 1.37, since $N$ is normal)
2. $H \cap N$ is normal in $H$ (it is the kernel of $H \to G/N$)
3. The isomorphism $H/(H \cap N) \cong HN/N$ comes from restricting the canonical map

# Construction / Recognition

## Proof Sketch:
1. Consider the homomorphism $H \to G/N$ given by $h \mapsto hN$
2. Its kernel is $H \cap N$
3. Its image is $\{hN \mid h \in H\} = HN/N$
4. Apply the factorization theorem

# Context & Application

This theorem is useful whenever you have a subgroup and a normal subgroup interacting. It relates the "overlap" $H \cap N$ to the "combined" group $HN$.

# Examples

**Example 1**: If $G = \mathbb{Z}$, $H = m\mathbb{Z}$, $N = n\mathbb{Z}$, then $HN = \gcd(m,n)\mathbb{Z}$, $H \cap N = \mathrm{lcm}(m,n)\mathbb{Z}$, and the theorem gives $m\mathbb{Z}/\mathrm{lcm}(m,n)\mathbb{Z} \cong \gcd(m,n)\mathbb{Z}/n\mathbb{Z}$.

# Relationships

## Builds Upon
- **normal-subgroup**, **quotient-group**, **factorization-theorem**

## Related
- **correspondence-theorem** — another isomorphism theorem

# Common Errors

- **Error**: Forgetting that $N$ must be normal in $G$ (or at least normalized by $H$)
  **Correction**: If $N$ is not normal, $HN$ may not be a subgroup. However, it suffices that $hNh^{-1} = N$ for all $h \in H$ (p. 22)

# Source Reference

Chapter 1, Theorem 1.46, page 22.

# Verification Notes

- Definition source: Direct from Theorem 1.46
- Confidence: HIGH — explicit theorem
- Uncertainties: None
