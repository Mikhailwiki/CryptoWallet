SPECIAL_CHARACTERS = "!@#$%^&*()_+-=[]{}|;':\",.<>?/\\"
LOGS = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>741</width>
    <height>552</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="background_label">
    <property name="geometry">
     <rect>
      <x>-70</x>
      <y>-50</y>
      <width>901</width>
      <height>631</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QWidget" name="gridLayoutWidget">
    <property name="geometry">
     <rect>
      <x>180</x>
      <y>110</y>
      <width>381</width>
      <height>231</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="gridLayout">
     <item row="5" column="0">
      <layout class="QHBoxLayout" name="horizontalLayout">
       <item>
        <widget class="QPushButton" name="log_btn">
         <property name="text">
          <string>Log in</string>
         </property>
        </widget>
       </item>
       <item>
        <widget class="QPushButton" name="sign_btn">
         <property name="text">
          <string>Sign up</string>
         </property>
        </widget>
       </item>
      </layout>
     </item>
     <item row="2" column="0">
      <widget class="QLineEdit" name="username"/>
     </item>
     <item row="4" column="0">
      <widget class="QLineEdit" name="password"/>
     </item>
     <item row="3" column="0">
      <widget class="QLabel" name="label_2">
       <property name="text">
        <string>Password</string>
       </property>
      </widget>
     </item>
     <item row="1" column="0">
      <widget class="QLabel" name="label">
       <property name="text">
        <string>Login</string>
       </property>
      </widget>
     </item>
     <item row="0" column="0">
      <widget class="QLabel" name="result">
       <property name="text">
        <string/>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>741</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
USER_WALLET = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="background_label">
    <property name="geometry">
     <rect>
      <x>-20</x>
      <y>0</y>
      <width>821</width>
      <height>591</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QWidget" name="gridLayoutWidget">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>190</y>
      <width>461</width>
      <height>391</height>
     </rect>
    </property>
    <layout class="QGridLayout" name="gridLayout">
     <item row="2" column="0">
      <widget class="QLabel" name="label">
       <property name="text">
        <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:24pt;&quot;&gt;Wallet&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
       </property>
      </widget>
     </item>
     <item row="1" column="1">
      <widget class="QPushButton" name="send_btn">
       <property name="text">
        <string>Send</string>
       </property>
      </widget>
     </item>
     <item row="1" column="0">
      <widget class="QPushButton" name="get_btn">
       <property name="text">
        <string>Get</string>
       </property>
      </widget>
     </item>
     <item row="2" column="1">
      <widget class="QPushButton" name="update_btn">
       <property name="text">
        <string>Update</string>
       </property>
      </widget>
     </item>
     <item row="3" column="0" colspan="2">
      <widget class="QListWidget" name="listWidget"/>
     </item>
     <item row="0" column="0" colspan="2">
      <widget class="QPushButton" name="delete_btn">
       <property name="text">
        <string>Delete Account</string>
       </property>
      </widget>
     </item>
    </layout>
   </widget>
   <widget class="QLabel" name="login">
    <property name="geometry">
     <rect>
      <x>10</x>
      <y>10</y>
      <width>351</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="excange_rate">
    <property name="geometry">
     <rect>
      <x>460</x>
      <y>-20</y>
      <width>321</width>
      <height>311</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
GET_ADDRESS_UI = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>475</width>
    <height>324</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>30</x>
      <y>40</y>
      <width>211</width>
      <height>51</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:24pt;&quot;&gt;Your address&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>90</x>
      <y>110</y>
      <width>341</width>
      <height>61</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="background_label">
    <property name="geometry">
     <rect>
      <x>-60</x>
      <y>-40</y>
      <width>571</width>
      <height>361</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>40</x>
      <y>100</y>
      <width>41</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <zorder>background_label</zorder>
   <zorder>label</zorder>
   <zorder>lineEdit</zorder>
   <zorder>pushButton</zorder>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>475</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
SEND_TO_ADDRESS_UI = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>428</width>
    <height>297</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>0</y>
      <width>171</width>
      <height>61</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:24pt;&quot;&gt;Put address&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QLineEdit" name="lineEdit">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>50</y>
      <width>281</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <widget class="QLabel" name="background_label">
    <property name="geometry">
     <rect>
      <x>-60</x>
      <y>-40</y>
      <width>521</width>
      <height>341</height>
     </rect>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QLabel" name="result">
    <property name="geometry">
     <rect>
      <x>20</x>
      <y>190</y>
      <width>231</width>
      <height>61</height>
     </rect>
    </property>
    <property name="styleSheet">
     <string notr="true"/>
    </property>
    <property name="text">
     <string/>
    </property>
   </widget>
   <widget class="QPushButton" name="send_btn">
    <property name="geometry">
     <rect>
      <x>270</x>
      <y>200</y>
      <width>121</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>Send</string>
    </property>
   </widget>
   <widget class="QLabel" name="label_2">
    <property name="geometry">
     <rect>
      <x>0</x>
      <y>90</y>
      <width>211</width>
      <height>41</height>
     </rect>
    </property>
    <property name="text">
     <string>&lt;html&gt;&lt;head/&gt;&lt;body&gt;&lt;p&gt;&lt;span style=&quot; font-size:24pt;&quot;&gt;Select amount&lt;/span&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
    </property>
   </widget>
   <widget class="QDoubleSpinBox" name="amount">
    <property name="geometry">
     <rect>
      <x>100</x>
      <y>131</y>
      <width>271</width>
      <height>31</height>
     </rect>
    </property>
   </widget>
   <zorder>background_label</zorder>
   <zorder>label</zorder>
   <zorder>lineEdit</zorder>
   <zorder>result</zorder>
   <zorder>send_btn</zorder>
   <zorder>label_2</zorder>
   <zorder>amount</zorder>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>428</width>
     <height>21</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>
'''
