import cv2

#Para leer el archivo de imágen
img =  cv2.imread("solar-system.jpg")

cv2.putText(img,
    "Sol",
    (100,80),
    cv2.FONT_HERSHEY_COMPLEX,
    2,
    (0,0,255)
)
cv2.putText(img,
    "Mercurio",
    (110,180),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)
cv2.putText(img,
    "Venus",
    (190,270),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)
cv2.putText(img,
    "Tierra",
    (290,270),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)
cv2.putText(img,
    "Marte",
    (380,170),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)
cv2.putText(img,
    "Jupiter",
    (570,45),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)
cv2.putText(img,
    "Saturno",
    (750,300),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)
cv2.putText(img,
    "Urano",
    (965,130),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)
cv2.putText(img,
    "Neptuno",
    (1110,140),
    cv2.FONT_HERSHEY_COMPLEX,
    0.5,
    (255,255,255)
)

#Para mostrar la imágen
cv2.imshow ("Output", img)

#Para guardar la imágen final
cv2.imwrite("Solar_systemwithname.jpg", img)

#Para que la imágen no se cierre
cv2.waitKey(0)