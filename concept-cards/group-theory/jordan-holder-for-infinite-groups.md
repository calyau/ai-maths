---
# === CORE IDENTIFICATION ===
concept: Jordan-Holder for Infinite Groups
slug: jordan-holder-for-infinite-groups

# === CLASSIFICATION ===
category: series-solvability
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Subnormal Series; Solvable and Nilpotent Groups"
chapter_number: 6
pdf_page: 88
section: "Subnormal Series"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - jordan-holder-theorem
  - composition-series
extends:
  - jordan-holder-theorem
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Does the Jordan-Holder theorem hold for infinite groups?"
---

# Quick Definition

The Jordan-Holder theorem extends to infinite groups that have finite composition series. The minimum length d(G) of a composition series is an invariant, and all composition series of length d(G) have isomorphic quotients. The proof uses induction on d(G) instead of |G|.

# Core Definition

**Remark 6.3(a).** There are infinite groups having finite composition series (there are even infinite simple groups). For such a group, let d(G) be the minimum length of a composition series. Then the Jordan-Holder theorem extends to show that all composition series have length d(G) and have isomorphic quotient groups. The same proof works except that you have to use induction on d(G) instead of |G| and verify that a normal subgroup of a group with a finite composition series also has a finite composition series (Exercise 6-1).

(Milne, Remark 6.3a, p. 88)

# Prerequisites

- **jordan-holder-theorem** -- the finite case
- **composition-series** -- existence of a finite composition series is the hypothesis

# Relationships

## Builds Upon
- **jordan-holder-theorem** -- generalization to infinite case

# Source Reference

Chapter 6, Remark 6.3(a), p. 88. Exercise 6-1.

# Verification Notes

- Definition source: Direct from Remark 6.3a
- Confidence rationale: HIGH -- explicit remark
- Uncertainties: None
