---
# === CORE IDENTIFICATION ===
concept: Quasi-Trivial Torus
slug: quasi-trivial-torus

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
pdf_page: 391
section: "Reductive algebraic groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - algebraic-torus
  - weil-restriction-of-scalars
extends:
  - algebraic-torus
related:
  - galois-cohomology-of-algebraic-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before understanding Galois cohomology of algebraic groups?"
---

# Quick Definition

A quasi-trivial torus over $k$ is a product of tori of the form $(\mathbb{G}_m)_{k'/k}$ for finite extensions $k'/k$. It has trivial $H^1$ over $k$ and all extensions of $k$.

# Core Definition

"A torus $T$ over a field $k$ is said to be *quasi-trivial* if it is a product of tori of the form $(\mathbb{G}_m)_{k'/k}$ with $k'$ a finite field extension of $k$." (Milne, p. 391)

If $T = \prod_i (\mathbb{G}_m)_{k_i/k}$, then $H^1(k, T) \simeq \prod_i H^1(k_i, \mathbb{G}_m) = 0$ by Shapiro's lemma and Hilbert 90.

# Prerequisites

- **Algebraic torus** — a quasi-trivial torus is a special type of torus
- **Weil restriction of scalars** — the building blocks $(\mathbb{G}_m)_{k'/k}$ are Weil restrictions

# Key Properties

1. $H^1(k, T) = 0$ for any quasi-trivial torus $T$
2. If $T$ is quasi-trivial over $k$, then $T_{k'}$ is quasi-trivial over $k'$ for any $k' \supset k$
3. Hence $H^1(k', T_{k'}) = 0$ for all extensions $k'/k$
4. A torus $T$ satisfies $H^1(k', T_{k'}) = 0$ for all $k' \supset k$ if and only if $T$ is a direct factor of a quasi-trivial torus (Theorem 1.18)

# Construction / Recognition

## To Construct:
1. Choose finite extensions $k_1, \ldots, k_r$ of $k$
2. Form $T = \prod_i (\mathbb{G}_m)_{k_i/k}$

## To Recognize:
1. Check if the torus $T$ splits as a product of Weil restrictions of $\mathbb{G}_m$ from finite extensions

# Context & Application

Quasi-trivial tori characterize the tori with universally vanishing $H^1$. They play a role in the structure theory of reductive groups, particularly in the classification of reductive groups via their centres and simply connected covers.

# Examples

**Example 1** (p. 391): $T = (\mathbb{G}_m)_{K/k}$ for a finite extension $K/k$ is quasi-trivial. Over $k^{\mathrm{al}}$, $T \simeq \mathbb{G}_m^{[K:k]}$.

# Relationships

## Builds Upon
- **Algebraic torus** — quasi-trivial tori are a special class of tori
- **Weil restriction of scalars** — built from Weil restrictions of $\mathbb{G}_m$

## Enables
- **Galois cohomology of algebraic groups** — provides vanishing results for $H^1$

# Common Errors

- **Error**: Assuming all split tori are quasi-trivial
  **Correction**: All split tori are quasi-trivial (take $k' = k$), but quasi-trivial tori need not be split

# Common Confusions

- **Confusion**: Confusing quasi-trivial with split
  **Clarification**: A quasi-trivial torus may not be split over $k$; it splits over the composite of the extensions $k_i$

# Source Reference

Chapter VI: The Structure of Reductive Groups: General Case, Section 1d "Tori," page 391. Theorem 1.18.

# Verification Notes

- Definition source: Direct quote from p. 391
- Confidence: HIGH — explicit definition
- Uncertainties: Theorem 1.18 proof omitted in source
- Cross-reference status: Verified
