---
# === CORE IDENTIFICATION ===
concept: Simple Group
slug: simple-group

# === CLASSIFICATION ===
category: group-structure
subcategory: group-classification
tier: intermediate

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Normal Subgroups and Factor Groups"
chapter_number: 10
pdf_page: 140
section: "The Simplicity of the Alternating Group"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normal-subgroup
  - group
extends: []
related:
  - simplicity-of-alternating-group
  - composition-series
  - solvable-group
contrasts_with:
  - solvable-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a simple group?"
  - "What distinguishes a simple group from a solvable group?"
---

# Quick Definition

A simple group is a group with no nontrivial proper normal subgroups. Simple groups are the "building blocks" of all finite groups, analogous to prime numbers for integers.

# Core Definition

"Of special interest are groups with no nontrivial normal subgroups. Such groups are called **simple groups**" (Judson, p. 140). A group $G$ is simple if its only normal subgroups are $\{e\}$ and $G$ itself.

# Prerequisites

- **Normal subgroup** — Simplicity is defined as absence of nontrivial normal subgroups
- **Group** — The base structure being classified

# Key Properties

1. The only normal subgroups of a simple group are $\{e\}$ and $G$
2. Every group of prime order $p$ is simple (since it has no proper subgroups at all)
3. The alternating group $A_n$ is simple for $n \geq 5$
4. Finite simple groups are the "building blocks" of all finite groups
5. The first nonabelian simple groups discovered were the alternating groups
6. A group of order $p^n$ (with $n > 1$) is never simple (it has a nontrivial center)

# Construction / Recognition

## To Determine if a Group is Simple:
1. List all normal subgroups of $G$
2. If the only normal subgroups are $\{e\}$ and $G$, then $G$ is simple
3. For abelian groups: $G$ is simple if and only if $G \cong \mathbb{Z}_p$ for some prime $p$
4. Use the Sylow theorems to detect normal subgroups (if there's a unique Sylow $p$-subgroup, it's normal)

# Context & Application

The classification of all finite simple groups is "one of the foremost problems of group theory" (p. 143) and was completed in the late 20th century. The classification shows that every finite simple group belongs to one of several infinite families (cyclic groups of prime order, alternating groups $A_n$ for $n \geq 5$, groups of Lie type) or is one of 26 sporadic groups (including the Monster group, a $196,883 \times 196,833$ matrix group).

# Examples

**Example 1** (p. 140): $\mathbb{Z}_p$ for $p$ prime is trivially simple since it has no proper subgroups other than $\{e\}$.

**Example 2** (p. 142): $A_n$ is simple for $n \geq 5$ (Theorem 10.11).

**Example 3** (p. 143): The Monster, one of 26 sporadic simple groups, is a $196,833 \times 196,833$ matrix group.

# Relationships

## Builds Upon
- **Normal subgroup** — Simplicity means no nontrivial normal subgroups

## Enables
- **Composition series** — The factors in a composition series are simple groups
- **Jordan-Holder theorem** — Relates composition series of a group

## Related
- **Classification of finite simple groups** — The grand program to find all simple groups

## Contrasts With
- **Solvable group** — A solvable group has a subnormal series with abelian factors; simple nonabelian groups are not solvable

# Common Errors

- **Error**: Assuming a group with no proper subgroups is the only kind of simple group
  **Correction**: A simple group may have proper subgroups; it just has no proper *normal* subgroups (other than $\{e\}$)

# Common Confusions

- **Confusion**: Thinking "simple" means "easy to understand"
  **Clarification**: Simple groups can be extremely complex (like the Monster). "Simple" means "cannot be decomposed further" via normal subgroups

# Source Reference

Chapter 10: Normal Subgroups and Factor Groups, Section 10.2, pages 140-143. Theorem 10.11 proves $A_n$ is simple for $n \geq 5$.

# Verification Notes

- Definition source: Direct quote from p. 140
- Historical notes from p. 143
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
