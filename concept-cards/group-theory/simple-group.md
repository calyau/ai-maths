---
# === CORE IDENTIFICATION ===
concept: Simple Group
slug: simple-group

# === CLASSIFICATION ===
category: subgroup-theory
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Group Theory"
source_slug: group-theory
authors: "J.S. Milne"
chapter: "Basic Definitions and Results"
chapter_number: 1
pdf_page: 19
section: "Normal subgroups"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normal-subgroup
extends: []
related:
  - quotient-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a simple group?"
  - "Can a simple group have nontrivial subgroups?"
---

# Quick Definition

A group $G$ is simple if it has no normal subgroups other than $G$ and $\{e\}$. Simple groups are the "atoms" of group theory.

# Core Definition

"A group $G$ is said to be **simple** if it has no normal subgroups other than $G$ and $\{e\}$." (Milne, p. 19)

# Prerequisites

- **Normal subgroup** — Simplicity is defined via normal subgroups

# Key Properties

1. A simple group can still have many nonnormal subgroups
2. Cyclic groups of prime order are simple (and the only abelian simple groups)
3. The Sylow theorems imply every finite group has nontrivial subgroups unless it is cyclic of prime order
4. The classification of finite simple groups is one of the great achievements of 20th-century mathematics

# Context & Application

Simple groups play the role in group theory that primes play in number theory. Every finite group can be built from simple groups via composition series (Jordan-Holder theorem).

# Examples

**Example 1**: $C_p$ is simple for any prime $p$ (it has no proper nontrivial subgroups at all).

**Example 2**: The alternating group $A_5$ is the smallest nonabelian simple group (order 60).

# Relationships

## Builds Upon
- **normal-subgroup** — simplicity means no proper nontrivial normal subgroups

## Related
- **quotient-group** — simple groups cannot be further decomposed via quotients

# Common Errors

- **Error**: Thinking "simple" means "no nontrivial subgroups"
  **Correction**: Simple means no nontrivial *normal* subgroups; nonnormal subgroups can exist

# Source Reference

Chapter 1, page 19.

# Verification Notes

- Definition source: Direct from p. 19
- Confidence: HIGH — explicit definition
- Uncertainties: None
