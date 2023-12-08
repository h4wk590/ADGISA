
## Aidan Brown
## GEOG 523 Fall 2023


## Agisoft Metashape Report


### Deliverables

- Object Choice
- Photo Acquisition/Quality/Lighting
- Modeling Details
- Model Export/Report

### Objective

This report summarizes the use and data extrapolated from performing 3D modeling on an object of choice. Presented in this report are findings and suggestions for the use of 3D modeling in Agisoft Metashape.

### Chosen Object

Chosen object was an aluminum can. I chose the object, as it's dimensions and shape are recognizable, but can still provide a solid foundation for modeling as it's cylindrical in nature with distinct features, but still provides some challenges when it comes to the accuracy of 3D modeling.

### Photo Acquisition 

#### Quantity and Geometry

12 Photos were taken at different angles to simulate different data locations if using a GPS unit, and to get a better perspective on the cylindrical shape. At first only 8 photos were taken, to replicate the example from the lab. This was too little and the points weren't properly populated when taking the example amount. 14 photos was enough to satisfy the software and I was able to add more points, while the other photos took these points as reference.

![Pasted image 20231205154423.png](../../attachments/Pasted%20image%2020231205154423.png)

(Fig 1. example photo out of the 14 taken.)

Photos were taken with default settings using a Google Pixel 4A smart phone. No extra steps or adjustments were needed to transfer photos to Agisoft.

#### Lighting Conditions

When viewing <i>Fig 1</i> you will find the white sheet of paper used as a backdrop. This was done purposely, as when first taking these photos **without** the software would pick up other point features that were in the photo frame. The white backdrop was used to keep the photo subject in frame and the only object in frame.


### Modeling

#### Modeling Steps

Once adding the photos to the new workspace in Agisoft, I first aligned the photos. No errors or extra points were created in doing this so I continued. I then added two points to measure the distance of the object. Two points near the top of the can from the both farthest distances as I could.

Once the two markers were placed I created a scalebar to measure the distance between the two points: 

![Pasted image 20231205155347.png](../../attachments/Pasted%20image%2020231205155347.png)
(Fig 2. Displaying the resulting distance between the two placed markers.)

Even though the white backdrop was a necessary step to accurately display the object, the software still provided points that were captured from the photos that skewed the accuracy of the image. I removed these points before continuing to fully model the object.

Once complete I ran the **Optimize Cameras** feature, which ran without error. From here I built out the point cloud, and mesh frames:

![Pasted image 20231205155712.png](../../attachments/Pasted%20image%2020231205155712.png)
(Fig 3. Displaying resulting mesh of the point cloud.)

While viewing <i>Fig 3</i> the white background, as well as some of the table surface was included in the point cloud. I was unable to remove both of these from the final object. The capture of the can object itself was fairly complete, capturing the smooth features of the can.

![Pasted image 20231205160133.png](../../attachments/Pasted%20image%2020231205160133.png)
(Fig 4. Viewing shaded model to showcase capturing the objects surface.)

### Conclusion

3D modeling of the aluminum can proved to be a successful demonstration of the use of Agisoft Metashape capabilities to accurately capture and display real objects. Besides some manual removal of additional points from the original images taken, the method in displaying the aluminum can object was overall successful.