---
# === CORE IDENTIFICATION ===
concept: Sporadic Groups and Strongly Regular Graphs
slug: sporadic-groups-strongly-regular

# === CLASSIFICATION ===
category: spectral-graph-theory
subcategory: algebraic-connections
tier: advanced

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Graphs, Groups and Matrices"
chapter_number: 8
pdf_page: 283
section: "VIII.3 Strongly Regular Graphs"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - strongly-regular-graph
  - automorphism-group-graph
extends: []
related: []
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are sporadic simple groups related to strongly regular graphs?"
---

# Quick Definition

Several sporadic simple groups arise as (index-2 subgroups of) automorphism groups of strongly regular graphs, including the McLaughlin group and the Suzuki group.

# Core Definition

Sporadic simple groups are those not in the infinite families (cyclic of prime order, alternating, groups of Lie type). Several are related to strongly regular graphs: a graph with parameters $(162, 105, 81)$ has the McLaughlin group (order 898,128,000) as an index-2 subgroup of its automorphism group; a graph with parameters $(416, 100, 96)$ has the Suzuki group (order 448,345,497,600) similarly (Bollobas, p. 283).

# Prerequisites

- **Strongly regular graph** -- The graphs involved
- **Automorphism group of a graph** -- The connection to groups

# Key Properties

1. McLaughlin group: related to srg(162, 105, 81)
2. Suzuki group: related to srg(416, 100, 96)
3. The group is a subgroup of index 2 of the automorphism group
4. These connections are part of the classification of finite simple groups

# Construction / Recognition

Not applicable -- these are existence results.

# Context & Application

The connection between sporadic simple groups and strongly regular graphs is one of the deep links between group theory and combinatorics. It illustrates why algebraic graph theory is important for pure group theory.

# Examples

**Example** (p. 283): The McLaughlin group acts on a strongly regular graph with 162 vertices, degree 105, and 81 common neighbors for non-adjacent pairs.

# Relationships

## Builds Upon
- **Strongly regular graph** -- The graph structure
- **Automorphism group of a graph** -- The group structure

## Enables
- Connections to the classification of finite simple groups

## Related
- None

## Contrasts With
- None

# Common Errors

- **Error**: Thinking every strongly regular graph is related to a sporadic group
  **Correction**: Most strongly regular graphs have small or trivial automorphism groups

# Common Confusions

- **Confusion**: Thinking the automorphism group IS the sporadic group
  **Clarification**: The sporadic group is typically an index-2 subgroup of the full automorphism group

# Source Reference

Chapter VIII, Section VIII.3, page 283.

# Verification Notes

- Definition source: Synthesized from p. 283
- Confidence rationale: Medium -- brief mention without detailed proof
- Uncertainties: Parameters cited without full verification
- Cross-reference status: Verified against source
