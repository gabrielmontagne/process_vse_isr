from argparse import ArgumentParser
from xyy import process_frame, start_server

def init():
    parser = ArgumentParser()
    parser.add_argument('--weights', default='gans', choices=[
    'psnr-large',
    'psnr-small',
    'noise-cancel',
    'gans'])

    args = parser.parse_args()

    if args.weights == 'gans':
        from ISR.models import RRDN
        model = RRDN(weights='gans')
    else:
        from ISR.models import RDN
        model = RDN(weights=args.weights)

    @process_frame
    def sr_pixels(pixs, config):
        return model.predict(pixs[:,:,:3])

def main():
    init()
    start_server()
    print('running module process_vse_isr')

if __name__ == '__main__':
    main()
