from crime_cctv.models import Crime_cctv_DTO
from common.services import CommonService

class Crime_cctv_Service(Crime_cctv_DTO):
    dto = Crime_cctv_DTO()

    # DF 생성하기
    def new_model(self, payload):
        this = self.dto
        this.context ='./data/'
        this.fname = payload
        pass







