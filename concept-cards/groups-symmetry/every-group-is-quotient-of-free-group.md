---
# === CORE IDENTIFICATION ===
concept: Every Group is a Quotient of a Free Group
slug: every-group-is-quotient-of-free-group

# === CLASSIFICATION ===
category: combinatorial-group-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Free Groups and Presentations"
chapter_number: 27
pdf_page: 173
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - free-group
  - homomorphism
  - first-isomorphism-theorem
extends: []
related:
  - presentation-of-a-group
  - defining-relations
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why does every group have a presentation?"
---

# Quick Definition

Every group G is isomorphic to a quotient F(X)/N of some free group, where X is a generating set for G and N is the kernel of the natural surjection F(X) -> G. This is the foundational result that makes group presentations possible.

# Core Definition

"Let G be a group and suppose X is a set of generators for G. There is a natural homomorphism pi from the free group F(X) to G which sends each reduced word x_1^{n_1} x_2^{n_2} ... x_k^{n_k} onto the corresponding product of group elements in G. This homomorphism is surjective because X generates G and, if N denotes its kernel, the First Isomorphism Theorem tells us that F(X)/N is isomorphic to G. Therefore every group is a quotient of some free group" (Armstrong, Ch. 27, p. 176).

# Prerequisites

- **Free group** -- F(X) is the free group on the generators
- **Homomorphism** -- pi: F(X) -> G is the natural surjection
- **First Isomorphism Theorem** -- Gives G = F(X)/N

# Key Properties

1. The surjection pi sends each word to the corresponding product in G
2. The kernel N consists of all words that evaluate to the identity in G
3. G = F(X)/N by the First Isomorphism Theorem
4. Any subset R of N whose normal closure is N gives a set of defining relations
5. This result is the theoretical foundation for the entire theory of presentations

# Construction / Recognition

## The Natural Surjection
1. Choose any generating set X for G
2. Define pi: F(X) -> G by pi(x_1^{n_1}...x_k^{n_k}) = x_1^{n_1}...x_k^{n_k} (now computed in G)
3. pi is surjective because X generates G
4. Let N = ker(pi)
5. Then G = F(X)/N

# Context & Application

This result, stated on a single line by Armstrong, is the conceptual foundation for the entire second half of Chapter 27. It explains why presentations work: specifying generators X and relations R determines a group F(X)/N because N is the normal closure of R. Every group can be described this way.

# Examples

**Example 1** (p. 176): D_n = F({r,s})/N where N is the normal closure of {r^n, s^2, (rs)^2}.

**Example 2** (p. 176): Z = F({x})/N where N = {e} (trivial kernel; Z is already free).

**Example 3** (p. 176): Z_n = F({x})/N where N is the normal closure of {x^n}.

# Relationships

## Builds Upon
- **Free group** -- Every group is a quotient of a free group
- **First Isomorphism Theorem** -- Gives the isomorphism G = F(X)/N

## Enables
- **Presentation of a group** -- The theoretical justification for presentations
- **Defining relations** -- R generates N as a normal subgroup

# Common Errors

- **Error**: Thinking the quotient F(X)/N depends on the choice of X
  **Correction**: Different choices of X give different free groups and different N, but the quotient is always isomorphic to G

# Common Confusions

- **Confusion**: Thinking this means every group IS a free group
  **Clarification**: Every group is a QUOTIENT of a free group; the quotient kills the elements of N, imposing relations

# Source Reference

Chapter 27: Free Groups and Presentations, page 176 (pdf p. 176).

# Verification Notes

- Statement: Directly quoted from Armstrong p. 176
- Confidence: HIGH -- explicit statement
- Cross-references: Verified against planned extractions
- Uncertainties: None
