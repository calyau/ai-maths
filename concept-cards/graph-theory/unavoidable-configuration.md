---
concept: Unavoidable Configuration
slug: unavoidable-configuration
category: graph-colouring
subcategory: planar-colouring
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Colouring"
chapter_number: 5
pdf_page: 122
section: "Notes"
extraction_confidence: medium
aliases:
  - "reducible configuration"
prerequisites:
  - four-colour-theorem
  - plane-triangulation
extends: []
related:
  - four-colour-problem-history
contrasts_with: []
answers_questions:
  - "How is the four colour theorem proved?"
  - "What are unavoidable and reducible configurations?"
---

# Quick Definition
In the proof of the four colour theorem, an unavoidable set of configurations is a collection such that every plane triangulation contains at least one. A reducible configuration is one that can always be 4-coloured by induction. The proof shows that an unavoidable set of reducible configurations exists.

# Core Definition
"The proof sets out first to show that every plane triangulation must contain at least one of 1482 certain 'unavoidable configurations'. In a second step, a computer is used to show that each of those configurations is 'reducible', i.e., that any plane triangulation containing such a configuration can be 4-coloured by piecing together 4-colourings of smaller plane triangulations" (Diestel, Notes, p. 137).

# Prerequisites
- **Four colour theorem**, **Plane triangulation**

# Key Properties
1. Unavoidable: every triangulation contains at least one
2. Reducible: containing one guarantees 4-colourability by induction
3. The original proof used ~1500 configurations
4. Robertson et al. reduced this to 633 configurations
5. Reducibility is checked by computer

# Context & Application
The unavoidable/reducible framework is the paradigm for proving the 4CT. Finding the right set of configurations and proving their reducibility required both theoretical insight and massive computation.

# Relationships
## Related
- **Four colour problem history**

# Source Reference
Chapter 5, Notes, page 137.

# Verification Notes
- From Notes section
- Confidence: MEDIUM -- described in notes, not main text
