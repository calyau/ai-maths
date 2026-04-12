---
# === CORE IDENTIFICATION ===
concept: Simple Group
slug: simple-group

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
extends: []
related:
  - alternating-group
  - commutator-subgroup
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a simple group?"
  - "Why is A5 simple?"
---

# Quick Definition

A simple group is one whose only normal subgroups are $\{e\}$ and the group itself. Simple groups are the "building blocks" of all finite groups.

# Core Definition

A **simple group** is one whose only normal subgroups are $\{e\}$ and the whole group (Armstrong, Ch. 15, Exercise 15.12, p. 92).

# Prerequisites

- **Normal subgroup** — Simple groups are defined in terms of normal subgroups

# Key Properties

1. A simple group has no proper non-trivial normal subgroups
2. Every group of prime order is simple (its only subgroups are $\{e\}$ and itself)
3. $A_4$ is not simple: $V = \{\varepsilon, (12)(34), (13)(24), (14)(23)\}$ is a proper normal subgroup
4. $A_5$ is simple (Exercise 15.12)
5. $A_n$ is simple for all $n \ge 5$

# Construction / Recognition

## To Check Simplicity:
1. Find all normal subgroups of $G$
2. If only $\{e\}$ and $G$ are normal, then $G$ is simple

## Armstrong's Outline for $A_5$ (Exercise 15.12):
1. Compute specific commutators to show any non-trivial normal subgroup contains a 3-cycle
2. Show that 3-cycles in $A_5$ form a single conjugacy class (Exercise 14.5)
3. Conclude the normal subgroup must be all of $A_5$

# Context & Application

Armstrong introduces simple groups via the exercises, asking the reader to find a proper normal subgroup of $A_4$ and then prove $A_5$ is simple. The simplicity of $A_5$ is connected to the insolvability of the quintic equation by radicals, one of the great results of 19th-century algebra.

# Examples

**Example 1** (Exercise 15.12): $A_4$ has the proper normal subgroup $V$, so $A_4$ is NOT simple.

**Example 2** (Exercise 15.12): $A_5$ is simple. Any non-trivial normal subgroup must contain a 3-cycle, and since 3-cycles form a single conjugacy class in $A_5$, the subgroup must contain all 3-cycles, hence all of $A_5$.

# Relationships

## Builds Upon
- **Normal subgroup** — Simplicity is defined by the absence of proper normal subgroups

## Related
- **Alternating group** — $A_n$ is simple for $n \ge 5$
- **Commutator subgroup** — If $[G,G] = G$ and $G$ is non-abelian simple, then $G$ equals its commutator subgroup

# Common Errors

- **Error**: Thinking simple groups have no subgroups at all
  **Correction**: Simple groups can have many subgroups; the condition is that none (other than $\{e\}$ and $G$) are *normal*

# Common Confusions

- **Confusion**: Thinking "simple" means "easy to understand"
  **Clarification**: "Simple" is a technical term meaning no proper non-trivial normal subgroups. Simple groups can be very large and complicated (e.g., the Monster group).

# Source Reference

Chapter 15: Quotient Groups, Exercise 15.12, pp. 92-93 (pdf).

# Verification Notes

- Definition source: Direct from Exercise 15.12
- Confidence rationale: HIGH — explicitly defined, though details are exercises
- Uncertainties: The proof of $A_5$ simplicity is left as an exercise
