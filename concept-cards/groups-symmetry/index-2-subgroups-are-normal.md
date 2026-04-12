---
# === CORE IDENTIFICATION ===
concept: Index-2 Subgroups Are Normal
slug: index-2-subgroups-are-normal

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
  - index-of-subgroup
  - left-equals-right-cosets-iff-normal
extends:
  - normal-subgroup
related:
  - alternating-group
  - special-orthogonal-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When is a subgroup automatically normal?"
  - "Why is $A_n$ normal in $S_n$?"
---

# Quick Definition

Any subgroup of index 2 in a group $G$ is automatically a normal subgroup, and the quotient group is isomorphic to $\mathbb{Z}_2$.

# Core Definition

**(15.4) Theorem.** If the index of $H$ in $G$ is equal to 2, then $H$ is a normal subgroup of $G$ and the quotient group $G/H$ is isomorphic to $\mathbb{Z}_2$ (Armstrong, Ch. 15, p. 88).

**Proof.** For $x \in H$, clearly $xH = H = Hx$. For $x \in G - H$, the left cosets $H, xH$ partition $G$, and so do the right cosets $H, Hx$. Therefore $xH = G - H = Hx$. Since $xH = Hx$ for all $x$, $H$ is normal by Theorem (15.3). There are only two cosets, so $G/H \cong \mathbb{Z}_2$.

# Prerequisites

- **Normal subgroup** — The property being established
- **Index of a subgroup** — The hypothesis is that the index is 2
- **Left equals right cosets iff normal** — The tool used in the proof

# Key Properties

1. Any subgroup containing exactly half the elements of $G$ is normal
2. The proof requires no computation of conjugacy classes
3. The quotient group $G/H$ always has order 2, hence is $\mathbb{Z}_2$

# Construction / Recognition

## To Apply:
1. Check that $[G:H] = 2$ (equivalently, $|H| = |G|/2$ for finite groups)
2. Conclude $H \triangleleft G$ and $G/H \cong \mathbb{Z}_2$

# Context & Application

This is one of the most useful sufficient conditions for normality. Armstrong immediately applies it to three important cases.

# Examples

**Example 1** (p. 89): $A_n \triangleleft S_n$ because $[S_n : A_n] = 2$.

**Example 2** (p. 89): $\langle r \rangle \triangleleft D_n$ because $[D_n : \langle r \rangle] = 2$.

**Example 3** (p. 89): $SO_n \triangleleft O_n$ because $[O_n : SO_n] = 2$.

# Relationships

## Builds Upon
- **Normal subgroup** — Provides a sufficient condition

## Enables
- **$A_n \triangleleft S_n$** — Immediate application
- **$\langle r \rangle \triangleleft D_n$** — Immediate application
- **$SO_n \triangleleft O_n$** — Immediate application
- **Classification of groups of order $2p$** — Theorem (15.5) uses index-2 normality

# Common Errors

- **Error**: Trying to generalise to index 3 or higher
  **Correction**: Index-3 subgroups are NOT automatically normal. The proof relies on there being exactly two cosets.

# Common Confusions

- **Confusion**: Thinking the converse holds — that normal subgroups must have index 2
  **Clarification**: Normal subgroups can have any index. $\{e\}$ is always normal with index $|G|$.

# Source Reference

Chapter 15: Quotient Groups, Theorem (15.4), p. 88 (pdf). Examples (v)-(vii).

# Verification Notes

- Definition source: Direct from Theorem (15.4)
- Confidence rationale: HIGH — explicit theorem with proof and applications
- Uncertainties: None
