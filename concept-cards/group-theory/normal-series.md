---
# === CORE IDENTIFICATION ===
concept: Normal Series
slug: normal-series

# === CLASSIFICATION ===
category: series-solvability
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Subnormal Series; Solvable and Nilpotent Groups"
chapter_number: 6
pdf_page: 86
section: "Subnormal Series"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - invariant series

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
  - normal-subgroup
  - subnormal-series
extends:
  - subnormal-series
related:
  - composition-series
  - derived-series
contrasts_with:
  - subnormal-series

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a normal series?"
  - "What is the difference between a subnormal series and a normal series?"
---

# Quick Definition

A normal series is a subnormal series where every term G_i is normal in G (not just in G_{i-1}). This is a strictly stronger condition than being a subnormal series.

# Core Definition

A chain G = G_0 superset G_1 superset ... superset G_n = {1} is a *normal series* if G_i is normal in G for every i.

(Milne, p. 86)

# Prerequisites

- **subnormal-series** -- a normal series is a subnormal series with an additional condition

# Key Properties

1. Every normal series is a subnormal series, but not conversely
2. In a normal series, G acts on each quotient G_i/G_{i+1} by conjugation
3. The derived series is an example of a normal series (each derived subgroup is characteristic, hence normal)

# Context & Application

Normal series arise naturally when considering characteristic subgroups or the derived series. The Jordan-Holder theorem for groups with operators (Example 6.29a) is about admissible composition series when G acts on itself by conjugation, which corresponds to normal composition series.

# Examples

**Example 1**: The derived series G superset G' superset G'' superset ... is a normal series (each G^(n) is characteristic in G).

**Example 2** (p. 97, 6.29a): When G acts on itself by conjugation, admissible subnormal series are precisely normal series.

# Relationships

## Builds Upon
- **subnormal-series** -- adds the condition of normality in G

## Enables
- **jordan-holder-for-a-groups** -- normal composition series via G-action

## Contrasts With
- **subnormal-series** -- subnormal only requires normality in the preceding term

# Source Reference

Chapter 6, p. 86.

# Verification Notes

- Definition source: Direct from p. 86
- Confidence rationale: HIGH -- explicit definition
- Uncertainties: None
