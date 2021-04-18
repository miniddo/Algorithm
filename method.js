Meteor.methods({

    async "Weather.getWeatherInfo" (doc) {
      
      // 3. 받아온 파라미터는 변수에 할당
      let { nx, ny } = doc;
      
      // 4. 다른 사람에게 응답으로 보내줄 객체
      // 주로 isSuccess, requestedAt, result, errMessage 사용
      let responseDoc = {
        isSuccess: true,           
        requestedAt: new Date(),
        result: null,
        errMessage: null
      };

      try {

        // 5. 공공 api 사용
        let url = `http://apis.data.go.kr/1360000/...base_time=2300&nx=${nx}&ny=${ny}`;
        let PGS = await HTTP.get(url);
        let pgsData = PGS.content;
  
        let resultCo$de = pgsData.response.header.resultCode;

        // 6. 결과에 따라 응답 결과를 다르게 해준다.
        if(resultCode == '00') {
            responseDoc.result = pgsData.body.items;
        } else {
            responseDoc.isSuccess = false;
            responseDoc.errMessage = 'resultCode Error';
        }   
        
        // 7. 리턴
        return responseDoc;
  
      } catch(err) {
        throw new Meteor.Error(err);
      }
    }

  });