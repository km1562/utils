from .compute_polygon_area import compute_polygon_area

def save_result_to_txt(txt_save_path,prediction,polygons):

    file = open(txt_save_path,'w')
    classes = prediction['instances'].pred_classes

    for i in range(len(classes)):
        if classes[i]==0:
            if len(polygons[i]) != 0:
                points = []
                for j in range(0,len(polygons[i][0]),2):
                    points.append([polygons[i][0][j],polygons[i][0][j+1]])
                points = np.array(points)
                area = compute_polygon_area(points)

                if area > 220:
                    str_out = ''
                    for pt in polygons[i][0]:
                        str_out += str(pt)
                        str_out += ','
                    file.writelines(str_out+'###')
                    file.writelines('\r\n')
    file.close()