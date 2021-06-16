from crime_cctv.service import Crime_cctv_Service
from crime_cctv.models import Crime_cctv_DTO

class Crime_cctv_Api(object):

    @staticmethod
    def main():
        util = Crime_cctv_Service
        dto = Crime_cctv_DTO
        while 1:
            menu = input('0-Exit\n'
                         '1-new-model\n'
                         '')
            if menu == '0':
                break
            elif menu == '1':
                dto.dframe = util.new_model('crime-cctv')
                Crime_cctv_Api.print_this(dto.dframe)
            else:
                pass

Crime_cctv_Api.main()