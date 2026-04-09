---
# === CORE IDENTIFICATION ===
concept: Centre of a Group
slug: centre-of-a-group

# === CLASSIFICATION ===
category: subgroup-theory
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 11
section: "Subgroups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - center of a group
  - "Z(G)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - subgroup
extends:
  - subgroup
related:
  - abelian-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the centre of a group?"
  - "Which elements of a group commute with all other elements?"
---

# Quick Definition

The centre Z(G) of a group G is the set of all elements that commute with every element of G. It is always a subgroup of G, and G is abelian if and only if Z(G) = G.

# Core Definition

The **centre** of a group G is the subset Z(G) = {g in G | gx = xg for all x in G}. It is a subgroup of G (Example 1.12, p. 11).

# Prerequisites

- **Group** — the centre is defined for a group
- **Subgroup** — Z(G) is a subgroup of G

# Key Properties

1. Z(G) is a subgroup of G
2. Z(G) is always abelian
3. G is abelian if and only if Z(G) = G
4. Z(G) = {e} is possible for non-abelian groups
5. Z(G) is a normal subgroup of G

# Construction / Recognition

## To Construct:
1. For each g in G, check if gx = xg for all x in G
2. Collect all such g into Z(G)

## To Recognize:
1. An element g is in Z(G) if and only if it commutes with every element of G

# Context & Application

The centre measures "how abelian" a group is. It plays an important role in the structure theory of groups, particularly in the theory of p-groups (where the centre is always nontrivial).

# Examples

**Example 1** (p. 11, 1.12): Z(G) = {g in G | gx = xg for all x in G} is a subgroup of G.

**Example 2**: For any abelian group G, Z(G) = G.

**Example 3**: For S_3, Z(S_3) = {e} since S_3 is the smallest non-abelian group.

# Relationships

## Builds Upon
- **subgroup** — Z(G) is a subgroup

## Enables
- Central series and nilpotent groups (later chapters)

## Related
- **abelian-group** — G is abelian iff Z(G) = G

# Common Confusions

- **Confusion**: Thinking the centre must be nontrivial
  **Clarification**: For many non-abelian groups (e.g., S_n for n >= 3), the centre is trivial ({e})

# Source Reference

Chapter 1: Basic Definitions and Results, Example 1.12, page 11.

# Verification Notes

- Definition source: Direct from Example 1.12, p. 11
- Confidence rationale: HIGH — explicitly defined with subgroup property stated
- Uncertainties: None
- Cross-reference status: Verified against planned cards
