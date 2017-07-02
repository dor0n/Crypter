# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainFrame
###########################################################################

class MainFrame ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Crypter Builder", pos = wx.DefaultPosition, size = wx.Size( 580,700 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer1.SetMinSize( wx.Size( 580,700 ) ) 
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer31 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel31 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		LanguageSettingsSizer = wx.StaticBoxSizer( wx.StaticBox( self.m_panel31, wx.ID_ANY, u"Language Settings" ), wx.HORIZONTAL )
		
		bSizer202 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.BuilderLanguageLabel = wx.StaticText( LanguageSettingsSizer.GetStaticBox(), wx.ID_ANY, u"Builder Language", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BuilderLanguageLabel.Wrap( -1 )
		self.BuilderLanguageLabel.SetFont( wx.Font( 9, 74, 90, 90, False, "Arial Unicode MS" ) )
		self.BuilderLanguageLabel.SetToolTipString( u"Major version number. This will be included in the filename of the produced Crypter binary" )
		
		bSizer202.Add( self.BuilderLanguageLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer202.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		BuilderLanguageChoiceChoices = [ u"English", u"Русский" ]
		self.BuilderLanguageChoice = wx.Choice( LanguageSettingsSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, BuilderLanguageChoiceChoices, 0 )
		self.BuilderLanguageChoice.SetSelection( 0 )
		bSizer202.Add( self.BuilderLanguageChoice, 0, wx.ALL, 5 )
		
		
		LanguageSettingsSizer.Add( bSizer202, 1, wx.EXPAND, 5 )
		
		bSizer2011 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.CrypterLanguageLabel = wx.StaticText( LanguageSettingsSizer.GetStaticBox(), wx.ID_ANY, u"Crypter Binary Language", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.CrypterLanguageLabel.Wrap( -1 )
		self.CrypterLanguageLabel.SetFont( wx.Font( 9, 74, 90, 90, False, "Arial Unicode MS" ) )
		self.CrypterLanguageLabel.SetToolTipString( u"Minor version number. This will be included in the filename of the produced Crypter binary" )
		
		bSizer2011.Add( self.CrypterLanguageLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer2011.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		CrypterBinaryLanguageChoiceChoices = [ u"English", u"Русский" ]
		self.CrypterBinaryLanguageChoice = wx.Choice( LanguageSettingsSizer.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, CrypterBinaryLanguageChoiceChoices, 0 )
		self.CrypterBinaryLanguageChoice.SetSelection( 0 )
		bSizer2011.Add( self.CrypterBinaryLanguageChoice, 0, wx.ALL, 5 )
		
		
		LanguageSettingsSizer.Add( bSizer2011, 1, wx.EXPAND, 5 )
		
		
		self.m_panel31.SetSizer( LanguageSettingsSizer )
		self.m_panel31.Layout()
		LanguageSettingsSizer.Fit( self.m_panel31 )
		bSizer31.Add( self.m_panel31, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer31, 1, wx.EXPAND, 5 )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.m_panel3 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		VersionInfoSizer = wx.StaticBoxSizer( wx.StaticBox( self.m_panel3, wx.ID_ANY, u"Version Information" ), wx.HORIZONTAL )
		
		bSizer20 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.MajorVersionLabel = wx.StaticText( VersionInfoSizer.GetStaticBox(), wx.ID_ANY, u"Major Version", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.MajorVersionLabel.Wrap( -1 )
		self.MajorVersionLabel.SetFont( wx.Font( 9, 74, 90, 90, False, "Arial Unicode MS" ) )
		self.MajorVersionLabel.SetToolTipString( u"Major version number. This will be included in the filename of the produced Crypter binary" )
		
		bSizer20.Add( self.MajorVersionLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer20.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.MajorVersionTextCtrl = wx.TextCtrl( VersionInfoSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20.Add( self.MajorVersionTextCtrl, 0, wx.ALL, 5 )
		
		
		VersionInfoSizer.Add( bSizer20, 1, wx.EXPAND, 5 )
		
		bSizer201 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.MinorVersionLabel = wx.StaticText( VersionInfoSizer.GetStaticBox(), wx.ID_ANY, u"Minor Version", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.MinorVersionLabel.Wrap( -1 )
		self.MinorVersionLabel.SetFont( wx.Font( 9, 74, 90, 90, False, "Arial Unicode MS" ) )
		self.MinorVersionLabel.SetToolTipString( u"Minor version number. This will be included in the filename of the produced Crypter binary" )
		
		bSizer201.Add( self.MinorVersionLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer201.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.MinorVersionTextCtrl = wx.TextCtrl( VersionInfoSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer201.Add( self.MinorVersionTextCtrl, 0, wx.ALL, 5 )
		
		
		VersionInfoSizer.Add( bSizer201, 1, wx.EXPAND, 5 )
		
		
		self.m_panel3.SetSizer( VersionInfoSizer )
		self.m_panel3.Layout()
		VersionInfoSizer.Fit( self.m_panel3 )
		bSizer3.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer3, 1, wx.EXPAND, 5 )
		
		bSizer12 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_panel41 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		BinarySettingsSizer = wx.StaticBoxSizer( wx.StaticBox( self.m_panel41, wx.ID_ANY, u"Binary Settings" ), wx.VERTICAL )
		
		bSizer391 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer412 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer203213 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.FilenameLabel = wx.StaticText( BinarySettingsSizer.GetStaticBox(), wx.ID_ANY, u"Filename", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FilenameLabel.Wrap( -1 )
		self.FilenameLabel.SetFont( wx.Font( 9, 74, 90, 90, False, "Arial Unicode MS" ) )
		self.FilenameLabel.SetToolTipString( u"The name of the file (excluding the extension) to use for the produced Crypter binary" )
		
		bSizer203213.Add( self.FilenameLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer203213.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.FilenameTextCtrl = wx.TextCtrl( BinarySettingsSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer203213.Add( self.FilenameTextCtrl, 0, wx.ALL, 5 )
		
		
		bSizer412.Add( bSizer203213, 1, wx.EXPAND, 5 )
		
		bSizer2032112 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.ExtensionLabel = wx.StaticText( BinarySettingsSizer.GetStaticBox(), wx.ID_ANY, u"Extension", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.ExtensionLabel.Wrap( -1 )
		self.ExtensionLabel.SetFont( wx.Font( 9, 74, 90, 90, False, "Arial Unicode MS" ) )
		self.ExtensionLabel.SetToolTipString( u"The file extension of the Crypter binary, such as pdf or mp3. It is recommended that the extension matches the specified icon file" )
		
		bSizer2032112.Add( self.ExtensionLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer2032112.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.ExtensionTextCtrl = wx.TextCtrl( BinarySettingsSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2032112.Add( self.ExtensionTextCtrl, 0, wx.ALL, 5 )
		
		
		bSizer412.Add( bSizer2032112, 1, wx.EXPAND, 5 )
		
		
		bSizer391.Add( bSizer412, 1, wx.EXPAND, 5 )
		
		bSizer41111 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer20321211 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.PyinstallerAesKeyLabel = wx.StaticText( BinarySettingsSizer.GetStaticBox(), wx.ID_ANY, u"Pyinstaller AES Key", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.PyinstallerAesKeyLabel.Wrap( -1 )
		self.PyinstallerAesKeyLabel.SetFont( wx.Font( 9, 74, 90, 90, False, "Arial Unicode MS" ) )
		self.PyinstallerAesKeyLabel.SetToolTipString( u"The AES key used by Pyinstaller to encrypt the Crypter script files. This field is optional, but provides Crypter with a layer of obfuscation" )
		
		bSizer20321211.Add( self.PyinstallerAesKeyLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer20321211.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.PyInstallerAesKeyTextCtrl = wx.TextCtrl( BinarySettingsSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20321211.Add( self.PyInstallerAesKeyTextCtrl, 0, wx.ALL, 5 )
		
		
		bSizer41111.Add( bSizer20321211, 1, wx.EXPAND, 5 )
		
		bSizer203211111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.IconLabel = wx.StaticText( BinarySettingsSizer.GetStaticBox(), wx.ID_ANY, u"Icon", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.IconLabel.Wrap( -1 )
		self.IconLabel.SetFont( wx.Font( 9, 74, 90, 90, False, "Arial Unicode MS" ) )
		self.IconLabel.SetToolTipString( u"The icon (.ico) file to use for the binary" )
		
		bSizer203211111.Add( self.IconLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer203211111.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.IconFilePicker = wx.FilePickerCtrl( BinarySettingsSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.ico", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE|wx.FLP_FILE_MUST_EXIST )
		bSizer203211111.Add( self.IconFilePicker, 0, wx.ALL, 5 )
		
		
		bSizer41111.Add( bSizer203211111, 1, wx.EXPAND, 5 )
		
		
		bSizer391.Add( bSizer41111, 1, wx.EXPAND, 5 )
		
		
		BinarySettingsSizer.Add( bSizer391, 1, wx.EXPAND, 5 )
		
		
		self.m_panel41.SetSizer( BinarySettingsSizer )
		self.m_panel41.Layout()
		BinarySettingsSizer.Fit( self.m_panel41 )
		bSizer12.Add( self.m_panel41, 1, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel4 = wx.Panel( self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		RansomwareSettingsSizer = wx.StaticBoxSizer( wx.StaticBox( self.m_panel4, wx.ID_ANY, u"Ransomware Settings" ), wx.VERTICAL )
		
		bSizer39 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer41 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer20321 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.EncryptedFileExtensionLabel = wx.StaticText( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, u"Encrypted File Extension", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.EncryptedFileExtensionLabel.Wrap( -1 )
		self.EncryptedFileExtensionLabel.SetFont( wx.Font( 9, 74, 90, 90, False, "Arial Unicode MS" ) )
		self.EncryptedFileExtensionLabel.SetToolTipString( u"The file extension to use after encrypting files. For example, \"locked\" will change the extension of all files to .locked once encrypted." )
		
		bSizer20321.Add( self.EncryptedFileExtensionLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer20321.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.EncryptedFileExtensionTextCtrl = wx.TextCtrl( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20321.Add( self.EncryptedFileExtensionTextCtrl, 0, wx.ALL, 5 )
		
		
		bSizer41.Add( bSizer20321, 1, wx.EXPAND, 5 )
		
		bSizer203211 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.WalletAddressLabel = wx.StaticText( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, u"Wallet Address", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WalletAddressLabel.Wrap( -1 )
		self.WalletAddressLabel.SetFont( wx.Font( 9, 74, 90, 90, False, "Arial Unicode MS" ) )
		self.WalletAddressLabel.SetToolTipString( u"The Bitcoin wallet address to be shown in the GUI following encryption" )
		
		bSizer203211.Add( self.WalletAddressLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer203211.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.WalletAddressTextCtrl = wx.TextCtrl( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer203211.Add( self.WalletAddressTextCtrl, 0, wx.ALL, 5 )
		
		
		bSizer41.Add( bSizer203211, 1, wx.EXPAND, 5 )
		
		
		bSizer39.Add( bSizer41, 1, wx.EXPAND, 5 )
		
		bSizer411 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer203212 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.BitcoinFeeLabel = wx.StaticText( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, u"Bitcoin Fee", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BitcoinFeeLabel.Wrap( -1 )
		self.BitcoinFeeLabel.SetFont( wx.Font( 9, 74, 90, 90, False, "Arial Unicode MS" ) )
		self.BitcoinFeeLabel.SetToolTipString( u"The Bitcoin ransom fee to charge. This fee will be shown in the GUI following encryption" )
		
		bSizer203212.Add( self.BitcoinFeeLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer203212.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.BitcoinFeeTextCtrl = wx.TextCtrl( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer203212.Add( self.BitcoinFeeTextCtrl, 0, wx.ALL, 5 )
		
		
		bSizer411.Add( bSizer203212, 1, wx.EXPAND, 5 )
		
		bSizer2032111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.KeyDestructionTimeLabel = wx.StaticText( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, u"Key Destruction Time (s)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.KeyDestructionTimeLabel.Wrap( -1 )
		self.KeyDestructionTimeLabel.SetFont( wx.Font( 9, 74, 90, 90, False, "Arial Unicode MS" ) )
		self.KeyDestructionTimeLabel.SetToolTipString( u"The Key Destruction time in seconds. This timer will be shown in the GUI following encryption" )
		
		bSizer2032111.Add( self.KeyDestructionTimeLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer2032111.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.KeyDestructionTimeTextCtrl = wx.TextCtrl( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2032111.Add( self.KeyDestructionTimeTextCtrl, 0, wx.ALL, 5 )
		
		
		bSizer411.Add( bSizer2032111, 1, wx.EXPAND, 5 )
		
		
		bSizer39.Add( bSizer411, 1, wx.EXPAND, 5 )
		
		bSizer4111 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer2032121 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.MaxFileSizeLabel = wx.StaticText( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, u"Max File Size to Encrypt", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.MaxFileSizeLabel.Wrap( -1 )
		self.MaxFileSizeLabel.SetFont( wx.Font( 9, 74, 90, 90, False, "Arial Unicode MS" ) )
		self.MaxFileSizeLabel.SetToolTipString( u"The maximum fille size, in megabytes, to encrypt. Files larger than this limit will not be encrypted" )
		
		bSizer2032121.Add( self.MaxFileSizeLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer2032121.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.MaxFileSizeTextCtrl = wx.TextCtrl( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2032121.Add( self.MaxFileSizeTextCtrl, 0, wx.ALL, 5 )
		
		
		bSizer4111.Add( bSizer2032121, 1, wx.EXPAND, 5 )
		
		bSizer20321111 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.FiletypesToEncryptLabel = wx.StaticText( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, u"Filetypes to Encrypt", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.FiletypesToEncryptLabel.Wrap( -1 )
		self.FiletypesToEncryptLabel.SetFont( wx.Font( 9, 74, 90, 90, False, "Arial Unicode MS" ) )
		self.FiletypesToEncryptLabel.SetToolTipString( u"A comma separated list of filetypes. Files with these extensions will be encrypted" )
		
		bSizer20321111.Add( self.FiletypesToEncryptLabel, 0, wx.ALL|wx.TOP, 7 )
		
		
		bSizer20321111.AddSpacer( ( 0, 0), 1, wx.EXPAND, 5 )
		
		self.FiletypesToEncryptTextCtrl = wx.TextCtrl( RansomwareSettingsSizer.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer20321111.Add( self.FiletypesToEncryptTextCtrl, 0, wx.ALL, 5 )
		
		
		bSizer4111.Add( bSizer20321111, 1, wx.EXPAND, 5 )
		
		
		bSizer39.Add( bSizer4111, 1, wx.EXPAND, 5 )
		
		
		RansomwareSettingsSizer.Add( bSizer39, 1, wx.EXPAND, 5 )
		
		
		self.m_panel4.SetSizer( RansomwareSettingsSizer )
		self.m_panel4.Layout()
		RansomwareSettingsSizer.Fit( self.m_panel4 )
		bSizer12.Add( self.m_panel4, 0, wx.EXPAND |wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer12, 0, wx.EXPAND, 5 )
		
		
		self.m_panel1.SetSizer( bSizer2 )
		self.m_panel1.Layout()
		bSizer2.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 4, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel4112 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel4112.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer172 = wx.BoxSizer( wx.VERTICAL )
		
		self.BuildProgressGauge = wx.Gauge( self.m_panel4112, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
		self.BuildProgressGauge.SetValue( 0 ) 
		bSizer172.Add( self.BuildProgressGauge, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel4112.SetSizer( bSizer172 )
		self.m_panel4112.Layout()
		bSizer172.Fit( self.m_panel4112 )
		bSizer1.Add( self.m_panel4112, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel411 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel411.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer17 = wx.BoxSizer( wx.VERTICAL )
		
		ConsoleBoxSizer = wx.StaticBoxSizer( wx.StaticBox( self.m_panel411, wx.ID_ANY, u"Console" ), wx.VERTICAL )
		
		self.ConsoleTextCtrl = wx.TextCtrl( ConsoleBoxSizer.GetStaticBox(), wx.ID_ANY, u"Ready...", wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.TE_MULTILINE|wx.TE_READONLY )
		self.ConsoleTextCtrl.SetForegroundColour( wx.Colour( 24, 249, 0 ) )
		self.ConsoleTextCtrl.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		ConsoleBoxSizer.Add( self.ConsoleTextCtrl, 1, wx.ALL|wx.EXPAND, 4 )
		
		
		bSizer17.Add( ConsoleBoxSizer, 1, wx.EXPAND, 5 )
		
		
		self.m_panel411.SetSizer( bSizer17 )
		self.m_panel411.Layout()
		bSizer17.Fit( self.m_panel411 )
		bSizer1.Add( self.m_panel411, 2, wx.EXPAND |wx.ALL, 5 )
		
		self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
		bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )
		
		self.m_panel4111 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.DOUBLE_BORDER|wx.TAB_TRAVERSAL )
		self.m_panel4111.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		
		bSizer171 = wx.BoxSizer( wx.VERTICAL )
		
		self.BuildButton = wx.Button( self.m_panel4111, wx.ID_ANY, u"BUILD", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.BuildButton.SetFont( wx.Font( 9, 74, 90, 90, False, "Arial" ) )
		
		bSizer171.Add( self.BuildButton, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_panel4111.SetSizer( bSizer171 )
		self.m_panel4111.Layout()
		bSizer171.Fit( self.m_panel4111 )
		bSizer1.Add( self.m_panel4111, 1, wx.ALL|wx.EXPAND, 10 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

###########################################################################
## Class EncryptFiletypesDialog
###########################################################################

class EncryptFiletypesDialog ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Encryptable Filetypes", pos = wx.DefaultPosition, size = wx.Size( 400,500 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MAXIMIZE_BOX|wx.MINIMIZE_BOX )
		
		self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.DefaultSize )
		self.SetFont( wx.Font( 9, 74, 90, 90, False, "Arial" ) )
		
		bSizer30 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer30.SetMinSize( wx.Size( 400,500 ) ) 
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u"Select the filetypes to encrypt", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )
		self.m_staticText15.SetFont( wx.Font( 10, 74, 90, 92, True, "Arial" ) )
		
		bSizer30.Add( self.m_staticText15, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 20 )
		
		self.SelectAllCheckbox = wx.CheckBox( self, wx.ID_ANY, u"Select All", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.SelectAllCheckbox.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer30.Add( self.SelectAllCheckbox, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		FiletypesSizer = wx.BoxSizer( wx.VERTICAL )
		
		self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.VSCROLL )
		self.m_scrolledWindow1.SetScrollRate( 5, 5 )
		bSizer32 = wx.BoxSizer( wx.VERTICAL )
		
		DocumentFilesSizer = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"Document Files" ), wx.VERTICAL )
		
		bSizer54 = wx.BoxSizer( wx.HORIZONTAL )
		
		bSizer332 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_checkBox52 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"DOCX", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer332.Add( self.m_checkBox52, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_checkBox42 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"DOC", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer332.Add( self.m_checkBox42, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_checkBox32 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer332.Add( self.m_checkBox32, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_checkBox22 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer332.Add( self.m_checkBox22, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		bSizer54.Add( bSizer332, 1, wx.EXPAND, 5 )
		
		bSizer331 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_checkBox51 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer331.Add( self.m_checkBox51, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_checkBox41 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer331.Add( self.m_checkBox41, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_checkBox31 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer331.Add( self.m_checkBox31, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_checkBox21 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer331.Add( self.m_checkBox21, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		bSizer54.Add( bSizer331, 1, wx.EXPAND, 5 )
		
		bSizer33 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_checkBox5 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.m_checkBox5, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_checkBox4 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.m_checkBox4, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_checkBox3 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.m_checkBox3, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		self.m_checkBox2 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"Check Me!", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.m_checkBox2, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
		
		
		bSizer54.Add( bSizer33, 1, wx.EXPAND, 5 )
		
		
		DocumentFilesSizer.Add( bSizer54, 1, wx.EXPAND, 5 )
		
		bSizer57 = wx.BoxSizer( wx.HORIZONTAL )
		
		
		bSizer57.AddSpacer( ( 0, 0), 2, wx.EXPAND, 5 )
		
		self.m_checkBox50 = wx.CheckBox( DocumentFilesSizer.GetStaticBox(), wx.ID_ANY, u"Select All", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_checkBox50.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial" ) )
		
		bSizer57.Add( self.m_checkBox50, 0, wx.ALL, 10 )
		
		
		DocumentFilesSizer.Add( bSizer57, 0, 0, 5 )
		
		
		bSizer32.Add( DocumentFilesSizer, 1, wx.EXPAND, 5 )
		
		ImageFileszSizer = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"Image Files" ), wx.VERTICAL )
		
		
		bSizer32.Add( ImageFileszSizer, 1, wx.EXPAND, 5 )
		
		VideoFilesSizer = wx.StaticBoxSizer( wx.StaticBox( self.m_scrolledWindow1, wx.ID_ANY, u"Video Files" ), wx.VERTICAL )
		
		
		bSizer32.Add( VideoFilesSizer, 1, wx.EXPAND, 5 )
		
		
		self.m_scrolledWindow1.SetSizer( bSizer32 )
		self.m_scrolledWindow1.Layout()
		bSizer32.Fit( self.m_scrolledWindow1 )
		FiletypesSizer.Add( self.m_scrolledWindow1, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer30.Add( FiletypesSizer, 1, wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer30 )
		self.Layout()
		
		self.Centre( wx.BOTH )
	
	def __del__( self ):
		pass
	

