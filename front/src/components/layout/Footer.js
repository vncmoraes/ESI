/*!
  =========================================================
  * Muse Ant Design Home - v1.0.0
  =========================================================
  * Product Page: https://www.creative-tim.com/product/muse-ant-design-Home
  * Copyright 2021 Creative Tim (https://www.creative-tim.com)
  * Licensed under MIT (https://github.com/creativetimofficial/muse-ant-design-Home/blob/main/LICENSE.md)
  * Coded by Creative Tim
  =========================================================
  * The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
*/

import { Layout, Row, Col } from "antd";
import { HeartFilled } from "@ant-design/icons";

function Footer() {
  const { Footer: AntFooter } = Layout;

  return (
    <AntFooter style={{ background: "#fafafa" }}>
      <Row className="just">
        <Col xs={24} md={12} lg={12}>
          <div className="copyright">
            © 2022, feito por João, Daiti, Barbie, Macedo, Vino, Tengan.
          </div>
        </Col>
        <Col xs={24} md={12} lg={12}>
          <div className="footer-menu">
          </div>
        </Col>
      </Row>
    </AntFooter>
  );
}

export default Footer;
