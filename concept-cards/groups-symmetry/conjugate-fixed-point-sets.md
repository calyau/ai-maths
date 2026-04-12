---
# === CORE IDENTIFICATION ===
concept: Conjugate Elements Fix Equal Points
slug: conjugate-fixed-point-sets

# === CLASSIFICATION ===
category: group-actions
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Counting Orbits"
chapter_number: 18
pdf_page: 105
section: "Theorem 18.2"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-action
  - fixed-point-set
extends: []
related:
  - counting-theorem
  - conjugacy-class
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why can I compute the Counting Theorem sum using only conjugacy class representatives?"
---

# Quick Definition

Conjugate group elements fix the same number of points: if $h = ugu^{-1}$, then $|X^g| = |X^h|$. This allows the Counting Theorem to be computed using conjugacy class representatives.

# Core Definition

**(18.2) Theorem.** Group elements which are conjugate fix the same number of points (Armstrong, p. 106).

If $ugu^{-1} = h$ and $g$ fixes $x$, then $h$ fixes $u(x)$. The map $u$ provides a bijection from $X^g$ to $X^h$, so $|X^g| = |X^h|$.

# Prerequisites

- **Group action** -- the theorem concerns an action of $G$ on $X$
- **Fixed-point set** -- the objects being compared

# Key Properties

1. $u$ sends $X^g$ bijectively to $X^h$ when $h = ugu^{-1}$
2. $|X^g|$ is constant on conjugacy classes of $G$
3. This allows the Counting Theorem sum to be reorganised by conjugacy classes

# Construction / Recognition

## Proof (p. 106):
1. Let $ugu^{-1} = h$ and suppose $g(x) = x$
2. Then $h(u(x)) = ugu^{-1}(u(x)) = ug(x) = u(x)$, so $u(x) \in X^h$
3. Thus $u$ maps $X^g$ into $X^h$
4. Reversing roles: $u^{-1}$ maps $X^h$ into $X^g$
5. Therefore $u$ is a bijection from $X^g$ to $X^h$

# Context & Application

This result is the computational workhorse behind the Counting Theorem. Instead of computing $|X^g|$ for every element of $G$, one need only compute it for one representative from each conjugacy class and multiply by the class size.

# Examples

**Emily's Problem** (p. 106): The 24 rotations of the cube fall into 5 conjugacy classes with representatives $e, r, r^2, s, t$. One computes $|X^g|$ only for these five.

# Relationships

## Builds Upon
- **Fixed-point set** -- the objects being compared
- **Group action** -- the context

## Enables
- **Counting theorem** -- allows efficient computation by conjugacy classes

# Source Reference

Chapter 18: Counting Orbits, Theorem 18.2, page 106.

# Verification Notes

- Theorem and proof: Direct from p. 106
- Confidence: HIGH -- explicit theorem with short proof
