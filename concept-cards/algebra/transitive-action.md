---
concept: Transitive Action
slug: transitive-action
category: symmetry
subcategory: group-actions
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Symmetry"
chapter_number: 6
pdf_page: 162
section: "6.7 Abstract Symmetry: Group Operations"
extraction_confidence: high
aliases: []
prerequisites:
  - group-action
  - orbit
extends:
  - group-action
related:
  - operation-on-cosets
contrasts_with: []
answers_questions:
  - "What is a transitive group action?"
---

# Quick Definition

A group action is transitive if S consists of a single orbit, meaning every element of S can be carried to every other by some group element.

# Core Definition

If S consists of just one orbit, the operation of G is called transitive. This means that every element of S is carried to every other one by some element of the group (Artin, p. 189). The symmetric group S_n acts transitively on {1, ..., n}. The isometry group M acts transitively on points and on lines, but not on triangles.

# Prerequisites

- **Group action** — Transitivity is a property of actions
- **Orbit** — A transitive action has one orbit

# Key Properties

1. For any s, s' in S, there exists g in G with gs = s'
2. |S| = |G| / |G_s| for any s in S
3. The action on cosets G/H is always transitive (Proposition 6.8.1)
4. Every transitive action is isomorphic to the action on cosets G/G_s

# Construction / Recognition

## To Verify:
1. Check that for any two elements s, s' in S, some g sends s to s'
2. Equivalently, check there is only one orbit

# Context & Application

Transitive actions are the "indecomposable" actions: any action decomposes into transitive actions on individual orbits. By Proposition 6.8.4, every transitive action is isomorphic to the action on cosets of the stabilizer.

# Examples

**Example 1** (p. 189): S_n acts transitively on {1, ..., n}.

**Example 2** (p. 192): The rotation group of a dodecahedron acts transitively on its faces, vertices, and edges.

# Relationships

## Builds Upon
- **Group action** — Transitivity is a property of actions

## Enables
- **Orbit-stabilizer bijection** — G/G_s is in bijection with the orbit (Proposition 6.8.4)

# Source Reference

Chapter 6: Symmetry, Section 6.7, p. 189.

# Verification Notes

- Definition source: Direct from p. 189
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
