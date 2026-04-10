---
# === CORE IDENTIFICATION ===
concept: Weil Restriction of Scalars
slug: weil-restriction-of-scalars

# === CLASSIFICATION ===
category: galois-cohomology
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Algebraic Groups, Lie Groups, and their Arithmetic Subgroups"
source_slug: groups-subgroups
authors: "J.S. Milne"
chapter: "The Structure of Reductive Groups: General Case"
chapter_number: 6
pdf_page: 390
section: "The cohomology of algebraic groups; applications"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - restriction of scalars
  - "Res_{K/k}"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - algebraic-group
extends: []
related:
  - galois-cohomology-of-algebraic-groups
  - quasi-trivial-torus
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding Galois cohomology of algebraic groups?"
---

# Quick Definition

The Weil restriction of scalars $G_*$ of an algebraic group $G$ over $K$ to $k$ (where $K/k$ is a finite extension) is the algebraic group over $k$ defined by $G_*(R) = G(K \otimes_k R)$. It converts a $K$-group into a $k$-group of larger dimension.

# Core Definition

Let $K$ be a finite extension of $k$ and $G$ an algebraic group over $K$. The Weil restriction $G_*$ is the algebraic group over $k$ with functor of points $G_*(R) = G(K \otimes_k R)$ for $k$-algebras $R$ (Milne, p. 390, referring to I, 4d).

Over $k^{\mathrm{al}}$, there is a canonical isomorphism:
$$G_{*k^{\mathrm{al}}} \simeq \prod_{\rho: K \to k^{\mathrm{al}}} \rho G$$
where $\rho$ ranges over $k$-homomorphisms $K \to k^{\mathrm{al}}$ (Proposition 1.16, p. 390).

# Prerequisites

- **Algebraic group** — Weil restriction takes an algebraic group over $K$ and produces one over $k$

# Key Properties

1. $G_*(R) = G(K \otimes_k R)$ as a functor on $k$-algebras
2. $\dim(G_*) = [K:k] \cdot \dim(G)$
3. $H^i(k, G_*) \simeq H^i(K, G)$ for $i = 0, 1$ (Shapiro's lemma, Corollary 1.17)
4. Over $k^{\mathrm{al}}$, $G_*$ splits as a product of Galois conjugates of $G$
5. If $G_{k'}$ is defined for $k' \supset k$, then $(G_*)_{k'} \simeq \prod G_{k'_i}$ where $k'_i$ are the factors of $K \otimes_k k'$

# Construction / Recognition

## To Construct:
1. Start with an algebraic group $G$ over a finite extension $K/k$
2. Define $G_*(R) = G(K \otimes_k R)$ for $k$-algebras $R$
3. This is representable by an algebraic group over $k$

## To Recognize:
1. An algebraic group $H$ over $k$ is a Weil restriction $G_*$ if $H_{k^{\mathrm{al}}} \simeq \prod_{\rho: K \to k^{\mathrm{al}}} \rho G$

# Context & Application

Weil restriction is used to study algebraic groups over extensions by reducing to the base field. It is essential in the theory of tori (quasi-trivial tori are products of Weil restrictions of $\mathbb{G}_m$) and in the study of almost-simple groups, where an almost-simple group over $k$ whose simple factors over $k^{\mathrm{al}}$ are permuted transitively by $\Gamma$ is a Weil restriction from the fixed field (Proposition 1.19).

# Examples

**Example 1** (p. 390): For $G = \mathbb{G}_m$ over $K$, the Weil restriction $(\mathbb{G}_m)_{K/k}$ has $(\mathbb{G}_m)_{K/k}(R) = (K \otimes_k R)^\times$.

**Example 2** (p. 392): If $G$ is an almost-simple, simply connected group over $k$ with $\Gamma$ acting transitively on its simple factors over $k^{\mathrm{al}}$, then $G \simeq G_{1*}$ where $G_1$ is geometrically almost-simple over a subfield $K$ (Proposition 1.19).

# Relationships

## Builds Upon
- **Algebraic group** — Weil restriction is a functor on algebraic groups

## Enables
- **Quasi-trivial torus** — defined as products of Weil restrictions of $\mathbb{G}_m$
- **Galois cohomology of algebraic groups** — Shapiro's lemma reduces cohomology via Weil restriction

# Common Errors

- **Error**: Forgetting that Weil restriction increases the dimension
  **Correction**: $\dim(G_*) = [K:k] \cdot \dim(G)$; for example, $(\mathbb{G}_m)_{\mathbb{C}/\mathbb{R}}$ is a 2-dimensional group over $\mathbb{R}$

# Common Confusions

- **Confusion**: Confusing Weil restriction with base change
  **Clarification**: Base change $G_K$ goes from $k$ to $K$ and preserves dimension; Weil restriction $G_*$ goes from $K$ to $k$ and multiplies dimension by $[K:k]$

# Source Reference

Chapter VI: The Structure of Reductive Groups: General Case, Section 1c-1d, pages 390-392. Proposition 1.16, Corollary 1.17, Proposition 1.19.

# Verification Notes

- Definition source: Direct from p. 390, referring to I, 4d
- Confidence: HIGH — explicit definition and key properties stated
- Uncertainties: None
- Cross-reference status: Verified
