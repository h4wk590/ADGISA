
## Aidan Brown
## GEOG 511 Fall 2023


## Dataset 1: Baseline Thematic Mapping

- **Must not overlap** - If the features overlapped it would no longer be true.
- **Must not contain gaps** - Data is continuous, and is based on the entire province any gaps wouldn't make sense on this map.

## Dataset 2: Census Data

- Census divisions should **not contain gaps**, as the data needs to be discrete and be contained within 1 division.
- The census areas **should not overlap** with each other.
- The census **Boundaries must be covered**.

## Dataset 3: Hydrological Data

- Flow gauge points - **must be covered by a line**, and **must be properly inside** of the watershed polygons.
- Steam Segment lines - **Must not have pseudo nodes**, and **must be properly inside** of the watershed polygons.
- Water Features - **Boundary must be covered by feature class** of flow gauge points and steam segment lines, and **must not have gaps**.
- Watersheds - **Must not overlap**, **contains point**, **Must be covered by** the water features feature class, Flow gauge points, and Steam Segment lines. 