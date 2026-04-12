---
# === CORE IDENTIFICATION ===
concept: Normality Checking via Generators
slug: normality-checking-via-generators

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
  - generator
extends:
  - normal-subgroup
related:
  - conjugation-by-g
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How can you efficiently check whether a subgroup is normal?"
---

# Quick Definition

To check that $H$ is normal in $G$, it suffices to verify $xhx^{-1} \in H$ for all $h \in H$ and all $x$ in a generating set for $G$ (provided the generating set is closed under inverses when $G$ is infinite).

# Core Definition

**(15.2) Theorem.** Let $H$ be a subgroup of $G$ and let $X$ be a set of generators for $G$ which, if $G$ is infinite, contains the inverse of each of its elements. Then $H$ is a normal subgroup of $G$, provided $xhx^{-1} \in H$ for all $h \in H$, $x \in X$ (Armstrong, Ch. 15, p. 88).

**Proof.** Express $g = x_1 x_2 \cdots x_t$ with each $x_i \in X$. Then $ghg^{-1} = x_1 \cdots x_t h x_t^{-1} \cdots x_1^{-1}$, and conjugation by $g$ amounts to repeated conjugation by elements of $X$. Each step stays in $H$ by assumption.

# Prerequisites

- **Normal subgroup** — The property being verified
- **Generator** — The generators of $G$

# Key Properties

1. Reduces checking infinitely many conjugations to finitely many (if $X$ is finite)
2. Requires the generating set to contain inverses when $G$ is infinite
3. Proof: conjugation by a product = repeated conjugation by factors

# Construction / Recognition

## To Apply:
1. Choose a generating set $X$ for $G$ (with inverses if $G$ is infinite)
2. For each $x \in X$ and each $h \in H$, check $xhx^{-1} \in H$
3. If all checks pass, $H \triangleleft G$

# Context & Application

This is a practical tool used in Example (iv): the subgroup $\langle r^2 \rangle$ of $D_n$ is shown to be normal by checking conjugation by the generators $r$ and $s$ only.

# Examples

**Example 1** (p. 88): $\langle r^2 \rangle$ is normal in $D_n$. Take $X = \{r, s\}$ and check: $r(r^{2k})r^{-1} = r^{2k}$ and $s(r^{2k})s = r^{-2k} \in \langle r^2 \rangle$.

# Relationships

## Builds Upon
- **Normal subgroup** — This is a criterion for normality

## Related
- **Conjugation by $g$** — The check involves conjugation by generators

# Common Errors

- **Error**: Forgetting to include inverses of generators when $G$ is infinite
  **Correction**: For infinite groups, the generating set must contain the inverse of each element (for finite groups, $x^{-1} = x^{|x|-1}$ is already a product of $x$'s)

# Common Confusions

- **Confusion**: Thinking it suffices to check $xhx^{-1} \in H$ for generators $h$ of $H$ as well
  **Clarification**: One must check all $h \in H$, not just generators of $H$ (though Exercise 15.10 gives a stronger result using generators of both)

# Source Reference

Chapter 15: Quotient Groups, Theorem (15.2), pp. 88-89 (pdf).

# Verification Notes

- Definition source: Direct from Theorem (15.2)
- Confidence rationale: HIGH — explicit theorem with proof and application
- Uncertainties: None
