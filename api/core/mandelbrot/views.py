
from flask import request
from mandelbrot import api

@api.route('/generate', methos=['GET'])
def generate():

    def isInMandelbrot(cr, ci, steps, bounds):
        '''
        cr -> starting real value
        ci -> starting imaginary value
        steps -> number of iterations to verify if value is in set
        bounds -> the escape radius of the mandelbrot
        '''
        zr = 0
        zi = 0
        tr = 0
        ti = 0
        n = 0

        # iterate the equation for the number of steps until value falls outside the escape radius
        for i in range(steps):
            
            if (tr * ti > bounds):
                return

            zi = 2 * zr * zi + ci
            zr = tr - ti + cr
            tr = zr * zr
            ti = zi * zi
            n += 1 # increase count of steps taken
        
        # Reduce error term by increasing number of iterations
        for i in range(steps):
            zi = 2 * zr * zi + ci
            zr = tr - ti + cr
            tr = zr * zr
            ti = zi * zi

        return [n, tr, ti]
    

    defaultLookAt = [0.6, 0]
    defaultZoom = [0, 0]

    width = request.args.get('width')
    height = request.args.get('height')
    maxIter = request.args.get('maxIter')
    lookAt = request.args.get('lookAt') or defaultLookAt
    zoom = request.args.get('zoom') or defaultZoom

    # xRange = 

    


    return []