---
concept: Sylow p-Subgroup
slug: sylow-p-subgroup
category: group-theory
subcategory: sylow-theory
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "More Group Theory"
chapter_number: 7
pdf_page: 206
section: "7.7 The Sylow Theorems"
extraction_confidence: high
aliases:
  - "Sylow subgroup"
prerequisites:
  - p-group
  - normalizer
extends: []
related:
  - first-sylow-theorem
  - second-sylow-theorem
  - third-sylow-theorem
contrasts_with: []
answers_questions:
  - "What is a Sylow subgroup?"
  - "What is a Sylow p-subgroup?"
---

# Quick Definition

A Sylow p-subgroup of a finite group G of order n = p^e * m (where p does not divide m) is a subgroup of order p^e. It is a p-group whose index is not divisible by p.

# Core Definition

Let G be a group of order n, and let p^e be the largest power of p dividing n, so n = p^e * m where m is not divisible by p. Subgroups H of G of order p^e are called Sylow p-subgroups of G. A Sylow p-subgroup is a p-group whose index in G is not divisible by p (Artin, (7.7.1), p. 217).

# Prerequisites

- **p-group** — A Sylow p-subgroup is a maximal p-subgroup
- **Normalizer** — Used in the Sylow theorems

# Key Properties

1. Order is p^e where p^e || n (p^e divides n but p^{e+1} does not)
2. Index [G : H] = m is not divisible by p
3. Sylow p-subgroups exist (First Sylow Theorem)
4. All Sylow p-subgroups are conjugate (Second Sylow Theorem)
5. The number of Sylow p-subgroups divides m and is congruent to 1 mod p (Third Sylow Theorem)

# Construction / Recognition

## To Find:
1. Determine p^e from |G| = p^e * m
2. Look for subgroups of order p^e
3. The Sylow theorems guarantee existence and constrain the count

# Context & Application

Sylow subgroups are the most important tool for analyzing the structure of finite groups. The Sylow theorems provide powerful constraints: existence (1st), conjugacy and maximality (2nd), and numerical restrictions on the count (3rd). They are used to classify groups of small order.

# Examples

**Example 1** (p. 218): In a group of order 15 = 3 * 5, the unique Sylow 3-subgroup and unique Sylow 5-subgroup are both normal, and G = C_3 x C_5 = C_15.

**Example 2** (p. 218): In a group of order 6, there is one Sylow 3-subgroup (normal) and either 1 or 3 Sylow 2-subgroups.

# Relationships

## Builds Upon
- **p-group** — A Sylow p-subgroup is a p-group of maximal order

## Enables
- **Classification of groups** — Sylow subgroups constrain group structure
- **Normal subgroup detection** — Unique Sylow subgroup implies normality

# Common Errors

- **Error**: Assuming a p-subgroup is automatically a Sylow p-subgroup
  **Correction**: It must have order exactly p^e (the largest power of p dividing |G|)

# Common Confusions

- **Confusion**: Thinking Sylow p-subgroups are unique
  **Clarification**: They are unique only when s = 1; in general there are s >= 1 conjugate Sylow p-subgroups

# Source Reference

Chapter 7: More Group Theory, Section 7.7, (7.7.1), pages 217-218.

# Verification Notes

- Definition source: Direct from (7.7.1)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
