import cv2
import numpy as np
class KeyPoints:
    def __init__(self):
        pass
    def stitch(self,images,loweratio=0.75,reprojThresh=4.0,showMatches=False):
        (imageB,imageA)=images
        (kpsA,featureA)=self.detect_KeyPoints(imageA)
        (kpsB,featureB)=self.detect_KeyPoints(imageB)
        M=self.matchPoints(kpsA,kpsB,featureA,featureB,loweratio,reprojThresh)
        if M is None:
            print("HAHAHAHAAHAHAHAHAAHAHAHAH")
            return None
        (matcher,H,status)=M
        result=cv2.warpPerspective(imageA,H,(imageA.shape[1]+imageB.shape[1],imageA.shape[0]))
        result[0:imageB.shape[0], 0:imageB.shape[1]] = imageB

        if showMatches:
            vis=self.draw_matches(imageA,imageB,kpsA,kpsB,matcher,status)
            return(result,vis)
        return result


    def detect_KeyPoints(self,image):
    #gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        #(imageA,imageB)=images
        descriptors=cv2.xfeatures2d.SIFT_create()
        (kps,features)=descriptors.detectAndCompute(image,None)
        kps=np.float32([kp.pt for kp in kps])
        return (kps,features)

    def matchPoints(self,kpsA,kpsB,featuresA,featuresB,loweratio,reprojthresh):
        #loweratio=0.75
        descriptor=cv2.DescriptorMatcher_create("BruteForce")
        raw_matches=descriptor.knnMatch(featuresA,featuresB,2)
        matcher=[]
        #print(raw_matches)
        for m in raw_matches:
            if len(m)==2 and m[0].distance< m[1].distance * loweratio:
                matcher.append((m[0].trainIdx,m[0].queryIdx))
        if len(matcher)>4:
            ptsA=np.float32([kpsA[i] for (_,i) in matcher])
            ptsB=np.float32([kpsB[i] for (i,_) in matcher])
            (H,status)=cv2.findHomography(ptsA,ptsB,cv2.RANSAC,reprojthresh)
            return (matcher,H,status)
        return None

    def draw_matches(self,imageA,imageB,kpsA,kpsB,matches,status):
        (hA,wA)=imageA.shape[:2]
        (hB,wB)=imageB.shape[:2]
        screen=np.zeros((max(hA,hB),wA+wB,3),dtype="uint8")
        screen[0:hA,0:wA]=imageA
        screen[0:hB,wA:]=imageB
        for ((trainIdx,queryIdx),s) in zip(matches,status):
            if s==1:    
                ptA=(int(kpsA[queryIdx][0]),int(kpsA[queryIdx][1]))
                ptB=(int(kpsB[trainIdx][0])+wA,int(kpsB[trainIdx][1]))
                cv2.line(screen,ptA,ptB,(255,0,0),1)
        return screen    
