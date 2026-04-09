---
# === CORE IDENTIFICATION ===
concept: Automorphisms of Cyclic Groups
slug: automorphisms-of-cyclic-groups

# === CLASSIFICATION ===
category: automorphisms-extensions
subcategory: automorphisms
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Automorphisms and Extensions"
chapter_number: 3
pdf_page: 44
section: "Automorphisms of cyclic groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - automorphism-group
  - cyclic-group
extends:
  - automorphism-group
related:
  - chinese-remainder-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the automorphism group of a cyclic group?"
---

# Quick Definition

The automorphism group of a cyclic group $C_n$ is isomorphic to the group of units $(\mathbb{Z}/n\mathbb{Z})^\times$.

# Core Definition

"For a cyclic group $G$ of order $n$, $\operatorname{Aut}(G) \simeq (\mathbb{Z}/n\mathbb{Z})^\times$. The automorphism of $G$ corresponding to $[m] \in (\mathbb{Z}/n\mathbb{Z})^\times$ is $a \mapsto a^m$" (Milne, Summary 3.5, p. 44).

# Prerequisites

- **Automorphism group** — This describes $\operatorname{Aut}(C_n)$ explicitly
- **Cyclic group** — The groups whose automorphisms are being classified

# Key Properties

1. $\operatorname{Aut}(C_n) \simeq (\mathbb{Z}/n\mathbb{Z})^\times$, independent of the choice of generator
2. If $n = p_1^{r_1} \cdots p_s^{r_s}$, then $(\mathbb{Z}/n\mathbb{Z})^\times \simeq \prod (\mathbb{Z}/p_i^{r_i}\mathbb{Z})^\times$ (CRT)
3. For odd prime $p$: $(\mathbb{Z}/p^r\mathbb{Z})^\times \approx C_{(p-1)p^{r-1}}$ (cyclic)
4. $(\mathbb{Z}/4\mathbb{Z})^\times \approx C_2$
5. For $r > 2$: $(\mathbb{Z}/2^r\mathbb{Z})^\times \approx C_2 \times C_{2^{r-2}}$
6. $|\operatorname{Aut}(C_n)| = \varphi(n)$ (Euler's totient function)

# Construction / Recognition

## To find $\operatorname{Aut}(C_n)$:
1. Factor $n = p_1^{r_1} \cdots p_s^{r_s}$
2. Apply $(\mathbb{Z}/n\mathbb{Z})^\times \simeq \prod (\mathbb{Z}/p_i^{r_i}\mathbb{Z})^\times$
3. Use Summary 3.5(c) for each prime power factor

# Examples

**Example 1** (p. 44): $\operatorname{Aut}(C_p) \simeq C_{p-1}$ for $p$ an odd prime.

**Example 2** (p. 44): $(\mathbb{Z}/8\mathbb{Z})^\times = \langle \bar{3}, \bar{5} \rangle \approx C_2 \times C_2$ is not cyclic.

# Relationships

## Builds Upon
- **automorphism-group**, **cyclic-group**

## Enables
- **semidirect-product** — Many semidirect products use homomorphisms $Q \to \operatorname{Aut}(C_n)$

# Common Errors

- **Error**: Assuming $(\mathbb{Z}/n\mathbb{Z})^\times$ is always cyclic
  **Correction**: It is not cyclic when $n$ is divisible by 8, or by two distinct odd primes

# Source Reference

Chapter 3: Automorphisms and Extensions, "Automorphisms of cyclic groups", Summary 3.5, page 44.

# Verification Notes

- Definition source: Summary 3.5, p. 44
- Confidence: HIGH — explicit statement
- Uncertainties: None
