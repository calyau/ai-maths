---
# === CORE IDENTIFICATION ===
concept: Left Equals Right Cosets iff Normal
slug: left-equals-right-cosets-iff-normal

# === CLASSIFICATION ===
category: normal-subgroups-quotients
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Quotient Groups"
chapter_number: 15
pdf_page: 86
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normal-subgroup
  - left-coset
  - right-coset
extends: []
related:
  - quotient-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When do left and right cosets coincide?"
  - "What is the equivalent condition for normality in terms of cosets?"
---

# Quick Definition

A subgroup $H$ of $G$ is normal if and only if $xH = Hx$ for every $x \in G$ — that is, the left and right cosets of $H$ coincide.

# Core Definition

**(15.3) Theorem.** The subgroup $H$ of $G$ is normal if and only if $xH = Hx$ for all $x \in G$ (Armstrong, Ch. 15, p. 88).

**Proof.** If $H$ is normal: for any $x \in G$, $h \in H$, the conjugates $xhx^{-1}$ and $x^{-1}hx$ belong to $H$. So $xh = (xhx^{-1})x \in Hx$, giving $xH \subseteq Hx$; similarly $hx = x(x^{-1}hx) \in xH$, giving $Hx \subseteq xH$.

Conversely, if $xH = Hx$ for all $x$: $xhx^{-1} \in (xH)x^{-1} = (Hx)x^{-1} = H$, so $H$ is normal.

# Prerequisites

- **Normal subgroup** — One side of the equivalence
- **Left coset** — $xH$
- **Right coset** — $Hx$

# Key Properties

1. This gives an equivalent characterisation of normality
2. Allows us to think of $G/H$ as either left or right cosets
3. The correspondence $xH \to Hx^{-1}$ is a bijection between left and right cosets even when $H$ is not normal

# Construction / Recognition

## To Check via This Criterion:
1. For each $x \in G$, verify $xH = Hx$ as sets
2. If this holds for all $x$, then $H$ is normal

# Context & Application

This characterisation is often the most natural way to verify normality. Armstrong uses it to prove Theorem (15.4): a subgroup of index 2 is normal, because the two left cosets ($H$ and $G - H$) must equal the two right cosets.

# Examples

**Example 1** (p. 88): For index-2 subgroups, $xH = Hx$ is automatic: if $x \in H$ both equal $H$; if $x \notin H$, both equal $G - H$.

# Relationships

## Builds Upon
- **Normal subgroup** — Equivalent characterisation

## Enables
- **Quotient group** — Can use either left or right cosets

## Related
- **Index-2 subgroups are normal** — Immediate corollary (Theorem 15.4)

# Common Errors

- **Error**: Interpreting $xH = Hx$ as element-wise commutativity
  **Correction**: $xH = Hx$ means the *sets* are equal. For each $h_1 \in H$ there exists $h_2 \in H$ with $xh_1 = h_2 x$, but generally $h_1 \neq h_2$.

# Common Confusions

- **Confusion**: Thinking left and right cosets are always different when $H$ is not normal
  **Clarification**: Some left cosets may equal the corresponding right cosets even for non-normal $H$; the point is that this must hold for ALL $x \in G$ simultaneously for normality.

# Source Reference

Chapter 15: Quotient Groups, Theorem (15.3), p. 88 (pdf).

# Verification Notes

- Definition source: Direct from Theorem (15.3)
- Confidence rationale: HIGH — explicit theorem with proof
- Uncertainties: None
