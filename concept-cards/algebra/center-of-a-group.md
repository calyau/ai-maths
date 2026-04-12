---
concept: Center of a Group
slug: center-of-a-group
category: group-theory
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Groups"
chapter_number: 2
pdf_page: 48
section: "2.5 Homomorphisms"
extraction_confidence: high
aliases:
  - "center"
  - "Z(G)"
prerequisites:
  - group
  - normal-subgroup
extends:
  - normal-subgroup
related:
  - abelian-group
  - conjugate
contrasts_with: []
answers_questions:
  - "What is a group?"
---

# Quick Definition

The center Z of a group G is the set of elements that commute with every element of G: Z = {z in G : zx = xz for all x in G}. It is always a normal subgroup.

# Core Definition

The center of a group G, often denoted Z, is the set {z in G : zx = xz for all x in G} (Artin, p. 63, formula 2.5.12). It is always a normal subgroup of G. The center of SL_2(R) is {I, -I}. The center of S_n is trivial for n >= 3.

# Prerequisites

- **Group** — The center is defined for any group
- **Normal subgroup** — The center is always normal

# Key Properties

1. Z is a normal subgroup of G
2. G is abelian iff Z = G
3. Z = {1} for S_n when n >= 3
4. Z(GL_n) = scalar matrices cI (c != 0)

# Construction / Recognition

## To Construct:
1. Find all elements z such that zg = gz for every g in G

## To Recognize:
1. The set of elements commuting with everything

# Context & Application

The center measures how close a group is to being abelian. It appears in the study of conjugacy classes and in the structure theory of groups.

# Examples

**Example 1** (p. 63): Z(SL_2(R)) = {I, -I}.

**Example 2** (p. 63): Z(S_n) = {1} for n >= 3.

# Relationships

## Builds Upon
- **Normal subgroup** — Center is always normal

## Related
- **Abelian group** — G is abelian iff G = Z(G)
- **Conjugate** — z is in center iff gzg^(-1) = z for all g

# Common Errors

- **Error**: Assuming the center is always nontrivial
  **Correction**: The center can be trivial ({1}), as in S_n for n >= 3

# Common Confusions

- **Confusion**: Confusing center with centralizer
  **Clarification**: The center commutes with ALL elements; a centralizer commutes with a specific element

# Source Reference

Chapter 2: Groups, Section 2.5, page 63.

# Verification Notes

- Definition source: Direct from (2.5.12), p. 63
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
