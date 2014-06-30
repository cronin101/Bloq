#include <OpenGL/gl.h>
#include <OpenGL/glu.h>
#include <GLUT/glut.h>
#include <vector>

void generateY0Plane(const int rows, const int cols,
        std::vector<float> &verts, std::vector<int> &idxs) {
    /* Generate vertices */
    for (int r = 0; r < rows; ++r)
        for (int c = 0; c < cols; ++c) {
            verts.push_back((float) c);
            verts.push_back(0.0f);
            verts.push_back((float) r);
        }

    /* Generate indices */
    for (int r = 0; r < rows-1; ++r) {
        /* Even rows */
        if ((r&1) == 0) {
            for (int c = 0; c < cols; ++c) {
                idxs.push_back(c + r*cols);
                idxs.push_back(c + (r + 1)*cols);
            }
        /* Odd rows */
        } else {
            for (int c = cols - 1; c > 0; --c) {
                idxs.push_back(c + (r + 1)*cols);
                idxs.push_back((c - 1) + r*cols);
            }
        }
    }
}

void renderY0Plane() {
    printf("Rendering Y0 Plane!\n");
    int width = 10, height = 10;
    std::vector<float> vertexes;
    std::vector<int> indices;
    printf("Generating data!\n");
    generateY0Plane(width, height, vertexes, indices);
    printf("Done!\n");
    for (auto it = vertexes.begin(); it != vertexes.end(); ++it)
        printf("%f\n", *it);
    for (auto it = indices.begin(); it != indices.end(); ++it)
        printf("%d\n", *it);
    glFrontFace(GL_CW);
    /*
    glBegin(GL_TRIANGLE_STRIP);
     
    glColor3f(1.0f, 0.0f, 0.0f);
    glVertex3f(-1.0f, -0.5f, -4.0f);    // A
     
    glColor3f(0.0f, 1.0f, 0.0f);
    glVertex3f( 1.0f, -0.5f, -4.0f);    // B
        
    glColor3f(0.0f, 0.0f, 1.0f);
    glVertex3f( 0.0f,  0.5f, -4.0f);    // C

    glColor3f(1.0f, 1.0f, 1.0f);
    glVertex3f( 1.0f,  0.5f, -4.0f);    // D
     
    glEnd();
    */

    glColor3f(1.0f, 1.0f, 1.0f);
    glEnableClientState(GL_COLOR_ARRAY);
    glVertexPointer(3, GL_FLOAT, 0, &vertexes[0]);
    glEnableClientState(GL_VERTEX_ARRAY);
    glDrawElements(GL_TRIANGLE_STRIP, 10/*vertexes.size()*/, GL_UNSIGNED_INT, &indices[0]);
    //glDisableClientState(GL_VERTEX_ARRAY);

}

void init() {
    glClearColor(0.0f, 0.0f, 0.0f, 0.0f);
    glEnable(GL_DEPTH_TEST);
    glShadeModel(GL_SMOOTH);
}

void display() {
    printf("Display tick!\n");
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    renderY0Plane();
    printf("Render complete\n");
    glutSwapBuffers();
}

void reshape(int w, int h) {
    glViewport(0, 0, w, h);
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glFrustum(-0.1, 0.1, -float(h)/(10.0*float(w)), float(h)/(10.0*float(w)), 0.5, 1000.0);
    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    int width = 640, height = 480;

    glutInitDisplayMode(GLUT_DOUBLE | GLUT_DEPTH | GLUT_RGBA);
    glutInitWindowSize(width, height);
    glutInitWindowPosition(0, 0);

    int window = glutCreateWindow(argv[0]);

    glutReshapeFunc(reshape);
    glutDisplayFunc(display);
    glutIdleFunc(display);

    init();
    glutMainLoop();

    return 0;
}
