---
# === CORE IDENTIFICATION ===
concept: Finitely Presented Group
slug: finitely-presented-group

# === CLASSIFICATION ===
category: free-groups-presentations
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Free Groups and Presentations; Coxeter Groups"
chapter_number: 2
pdf_page: 37
section: "Finitely presented groups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group-presentation
extends:
  - group-presentation
related:
  - word-problem
  - burnside-problem
  - todd-coxeter-algorithm
contrasts_with:
  - free-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a finitely presented group?"
  - "What distinguishes a free group from a finitely presented group?"
---

# Quick Definition

A group is finitely presented if it admits a presentation $\langle X \mid R \rangle$ with both $X$ and $R$ finite.

# Core Definition

"A group is said to be *finitely presented* if it admits a presentation $(X, R)$ with both $X$ and $R$ finite." (Milne, p. 37)

# Prerequisites

- **Group presentation** — a finitely presented group is one with a finite presentation

# Key Properties

1. Every finite group is finitely presented (Example 2.11): take $X = G$ and $R = \{abc^{-1} \mid ab = c \text{ in } G\}$
2. Properties of finitely presented groups can be very difficult to determine
3. There is no algorithm to decide if a finite presentation defines the trivial group
4. The word problem, finiteness, abelianness, etc. are generally undecidable

# Construction / Recognition

## To Show a Group is Finitely Presented:
1. Find finitely many generators $X$
2. Find finitely many relations $R$ such that $\langle X \mid R \rangle \cong G$

# Context & Application

Finitely presented groups arise naturally in topology (fundamental groups of compact manifolds), geometry, and combinatorial group theory. Despite their simple description, they can exhibit extremely complex behavior.

# Examples

**Example 1** (p. 37, Example 2.11): Any finite group $G$ is finitely presented with $X = G$ and $R = \{abc^{-1} \mid ab = c\}$.

**Example 2**: $D_n = \langle r, s \mid r^n, s^2, srsr \rangle$ is finitely presented (2 generators, 3 relations).

# Relationships

## Builds Upon
- **group-presentation**

## Enables
- **word-problem** — a decision problem for finitely presented groups
- **burnside-problem** — relates finite generation, finite exponent, and finiteness

## Contrasts With
- **free-group** — a free group has no relations; a finitely presented group has finitely many

# Common Errors

- **Error**: Assuming a finite presentation makes the group easy to analyze
  **Correction**: Milne warns that "calculating the properties of the group can be very difficult -- note that we are defining the group, which may be quite small, as the quotient of a huge free group by a huge subgroup" (p. 37)

# Source Reference

Chapter 2, pages 37-38. Example 2.11.

# Verification Notes

- Definition source: Direct from p. 37
- Confidence: HIGH
- Uncertainties: None
