// 1. 다른 사람이 나의 api로 접속할때 사용할 주소: ex) http://localhost:3000/api/weather
// 그 사람이 용인 날씨를 알고 싶다면 params 값에 용인의 nx, ny를 넣어서 나의 api를 조회해야함
// http://localhost:3000/api/weather?nx=62&ny=120
Picker.route('/api/weather', (params, req, res, next) => {

    let doc = {
        nx: params.query.nx,
        ny: params.query.ny
    }

    // 2. 다른 사람이 나의 api에 접속할 때 method는 get을 사용한다.
    switch(req.method) {
      case "GET":
        Meteor.call('Weather.getWeatherInfo', doc, (err, result) => {
          // 8. 접속자에게 리턴
          return result
        });
        break;
      // 2-1. get 방식이 아닌 method로 접근했을 때는 405 에러를 리턴한다.
      default:
        res.writeHead(405);
        res.end("Method Not Allowed");
    }
  
  });