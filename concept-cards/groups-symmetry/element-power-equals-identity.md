---
# === CORE IDENTIFICATION ===
concept: Element Power Equals Identity
slug: element-power-equals-identity

# === CLASSIFICATION ===
category: subgroup-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Lagrange's Theorem"
chapter_number: 11
pdf_page: 64
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$x^{|G|} = e$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - order-of-element-divides-group-order
extends:
  - lagrange-theorem
related:
  - euler-theorem
  - fermat-little-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What happens when you raise a group element to the power of the group's order?"
---

# Quick Definition

In a finite group $G$, raising any element to the power $|G|$ yields the identity: $x^{|G|} = e$ for all $x \in G$.

# Core Definition

**(11.4) Corollary.** If $x$ is an element of $G$ then $x^{|G|} = e$ (Armstrong, p. 65).

**Proof.** Let $m$ be the order of $x$. By Corollary (11.2), $|G| = km$ for some integer $k$. Hence $x^{|G|} = x^{km} = (x^m)^k = e$.

# Prerequisites

- **Order of element divides group order** — The proof depends on $m$ dividing $|G|$

# Key Properties

1. $x^{|G|} = e$ for every $x$ in a finite group $G$
2. This is the group-theoretic foundation of Euler's theorem and Fermat's little theorem

# Construction / Recognition

## To Apply:
1. Determine $|G|$
2. For any element $x$, $x^{|G|}$ must equal the identity

# Context & Application

This corollary provides the bridge from abstract group theory to number theory. Armstrong immediately applies it to the group $R_n$ of units modulo $n$ to derive Euler's theorem ($x^{\varphi(n)} \equiv 1 \pmod{n}$) and Fermat's little theorem ($x^{p-1} \equiv 1 \pmod{p}$).

# Examples

**Example 1** (p. 65): In $R_9 = \{1, 2, 4, 5, 7, 8\}$ with $\varphi(9) = 6$, we have $x^6 \equiv 1 \pmod{9}$ for all $x \in R_9$.

# Relationships

## Builds Upon
- **Lagrange's theorem** — Via the element-order corollary

## Enables
- **Euler's theorem** — Specialisation to $R_n$
- **Fermat's little theorem** — Specialisation to $R_p$

# Common Errors

- **Error**: Applying this to infinite groups
  **Correction**: The result requires $G$ to be finite. In infinite groups, there is no $|G|$ to raise elements to.

# Common Confusions

- **Confusion**: Thinking $|G|$ is the smallest power for which $x^n = e$
  **Clarification**: $|G|$ is generally not the order of $x$; it is merely a multiple of the order of $x$

# Source Reference

Chapter 11: Lagrange's Theorem, Corollary (11.4), p. 65 (pdf).

# Verification Notes

- Definition source: Direct from Corollary (11.4) with proof
- Confidence rationale: HIGH — explicit corollary
- Uncertainties: None
