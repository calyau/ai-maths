---
# === CORE IDENTIFICATION ===
concept: Convex Property
slug: convex-property

# === CLASSIFICATION ===
category: random-graphs
subcategory: property-types
tier: intermediate

# === PROVENANCE ===
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Graphs"
chapter_number: 7
pdf_page: 237
section: "VII.2 Simple Properties of Almost All Graphs"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gnp-model
extends: []
related:
  - monotone-increasing-property
  - equivalence-gnp-gnm
contrasts_with:
  - monotone-increasing-property

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a convex property of graphs?"
---

# Quick Definition

A set $\Omega^*$ of graphs is convex if $G \in \Omega^*$ whenever $G_1 \subset G \subset G_2$ and $G_1, G_2 \in \Omega^*$; a graph property is convex if the set of graphs having it is convex.

# Core Definition

A set $\Omega^* \subset \Omega$ is called convex if $G \in \Omega^*$ whenever $G_1 \subset G \subset G_2$ and $G_1, G_2 \in \Omega^*$ (Bollobás, p. 237). Convexity is the key condition for transferring "almost every" results from $\mathcal{G}(n, p)$ to $\mathcal{G}(n, M)$.

# Prerequisites

- **G(n,p) model** -- Context for the definition

# Key Properties

1. A convex property is closed under "sandwiching" between two graphs that have the property
2. Every monotone increasing property is convex (but not vice versa)
3. Convexity enables transfer from $\mathcal{G}(n, p)$ to $\mathcal{G}(n, \lfloor pN \rfloor)$ in Theorem 6

# Construction / Recognition

## To Verify Convexity
1. Take any two graphs $G_1, G_2$ with the property, where $G_1 \subset G_2$ (same vertex set)
2. Check that every graph $G$ with $G_1 \subset G \subset G_2$ also has the property

# Context & Application

Convexity is used in the proof that $\mathcal{G}(n, p)$ and $\mathcal{G}(n, M)$ results are interchangeable. Many natural properties are convex: having between $a$ and $b$ edges for fixed $a, b$ is convex but neither monotone increasing nor monotone decreasing.

# Examples

**Example** (p. 237): Having exactly $m$ edges is not convex, but having at least $m_1$ and at most $m_2$ edges is convex.

# Relationships

## Builds Upon
- **G(n,p) model** -- Setting for the definition

## Enables
- **Equivalence of G(n,p) and G(n,M)** -- Transfer principle for convex properties

## Related
- **Monotone increasing property** -- A stronger condition

## Contrasts With
- **Monotone increasing property** -- Monotone implies convex but not conversely

# Common Errors

- **Error**: Assuming all natural graph properties are convex
  **Correction**: Properties like "has exactly $k$ triangles" are not convex

# Common Confusions

- **Confusion**: Confusing convexity with monotonicity
  **Clarification**: Monotone increasing properties are convex, but convex properties need not be monotone

# Source Reference

Chapter VII: Random Graphs, Section VII.2, page 237.

# Verification Notes

- Definition source: Direct from p. 237
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
